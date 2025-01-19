import pygame
import json
from classes import MrX, Detective, Detective_Tickets, MrX_Tickets

# Initialize pygame
pygame.init()

# Get the current display info for fullscreen
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.RESIZABLE)
pygame.display.set_caption("Scotland-Yard Game")

# Constants
GRID_WIDTH, GRID_HEIGHT = 2500, 2000
MIN_ZOOM, MAX_ZOOM = 0.5, 5.0
SILVER = (220, 220, 220)  # Lighter background
WHITE, BLACK, RED, GREEN, BLUE, YELLOW = (255, 255, 255), (40, 40, 40), (220, 60, 60), (60, 220, 60), (60, 60, 220), (220, 220, 60)

# Add new colors
GRAY = (128, 128, 128)
NODE_INNER = (250, 250, 250)  # Inner node color
NODE_BORDER = (100, 100, 100)  # Node border color

# Update scaling constants with better fitting logic
def update_scaling():
    global scale_factor, offset_x, offset_y, MIN_ZOOM, MAX_ZOOM
    # Calculate scale factor to fit the entire map with some padding
    padding = 0.1  # 10% padding
    width_scale = WIDTH * (1 - padding) / GRID_WIDTH
    height_scale = HEIGHT * (1 - padding) / GRID_HEIGHT
    MIN_ZOOM = min(width_scale, height_scale)
    MAX_ZOOM = MIN_ZOOM * 5.0
    scale_factor = MIN_ZOOM
    
    # Center the map
    offset_x = (WIDTH - GRID_WIDTH * scale_factor) / 2
    offset_y = (HEIGHT - GRID_HEIGHT * scale_factor) / 2

def handle_resize(width, height):
    global WIDTH, HEIGHT
    WIDTH, HEIGHT = width, height
    update_scaling()
    
    # Ensure the map stays within bounds after resize
    global offset_x, offset_y
    max_offset_x = WIDTH - GRID_WIDTH * scale_factor
    max_offset_y = HEIGHT - GRID_HEIGHT * scale_factor
    offset_x = clamp(offset_x, max_offset_x, 0)
    offset_y = clamp(offset_y, max_offset_y, 0)

# Initialize scale and offset
update_scaling()

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

def zoom(factor):
    global scale_factor, offset_x, offset_y
    old_scale = scale_factor
    scale_factor = clamp(scale_factor * factor, MIN_ZOOM, MAX_ZOOM)
    
    # Adjust offset to keep the center point fixed when zooming
    center_x = WIDTH / 2
    center_y = HEIGHT / 2
    offset_x = center_x - (center_x - offset_x) * (scale_factor / old_scale)
    offset_y = center_y - (center_y - offset_y) * (scale_factor / old_scale)

# Load JSON data
try:
    with open("Final_Project/maps.json", "r") as file:
        game_map = json.load(file)
except FileNotFoundError:
    print("Error: Cannot find maps.json file")
    exit(1)

def draw_node(node, font, highlight=False, highlight_color=GREEN):
    x = int(node.get("position", {}).get("x", 0) * scale_factor + offset_x)
    y = int(node.get("position", {}).get("y", 0) * scale_factor + offset_y)

    # Draw node shadow
    pygame.draw.circle(screen, GRAY, (x + 2, y + 2), 15)
    
    # Main node circle
    color = highlight_color if highlight else NODE_INNER
    pygame.draw.circle(screen, color, (x, y), 15)
    pygame.draw.circle(screen, NODE_BORDER, (x, y), 15, 2)

    # Transport type indicators
    if any(edge["type"] == "bus" for edge in node.get("edges", [])):
        pygame.draw.circle(screen, BLUE, (x, y), 22, 2)
    if any(edge["type"] == "underground" for edge in node.get("edges", [])):
        pygame.draw.circle(screen, RED, (x, y), 27, 2)

    # Node number with better visibility
    text = font.render(str(node["id"]), True, BLACK)
    text_rect = text.get_rect(center=(x, y))
    # Add text shadow
    shadow_text = font.render(str(node["id"]), True, GRAY)
    shadow_rect = shadow_text.get_rect(center=(x + 1, y + 1))
    screen.blit(shadow_text, shadow_rect)
    screen.blit(text, text_rect)

def draw_edges(node, nodes_dict, edge_type):
    x1, y1 = int(node["position"]["x"] * scale_factor + offset_x), int(node["position"]["y"] * scale_factor + offset_y)
    for edge in node.get("edges", []):
        if edge["type"] != edge_type:
            continue
            
        to_node = nodes_dict.get(edge["to"])
        if not to_node:
            continue

        x2, y2 = int(to_node["position"]["x"] * scale_factor + offset_x), int(to_node["position"]["y"] * scale_factor + offset_y)
        
        if edge_type == "underground":
            width = 6
            color = RED
        elif edge_type == "bus":
            width = 4
            color = BLUE
        else:  # taxi
            width = 2
            color = BLACK

        pygame.draw.line(screen, color, (x1, y1), (x2, y2), width)

def draw_player(player, nodes_dict, color, index=None):
    node = nodes_dict.get(player.current_location())
    if node:
        x = int(node["position"]["x"] * scale_factor + offset_x)
        y = int(node["position"]["y"] * scale_factor + offset_y)
        
        # Draw player shadow
        pygame.draw.circle(screen, GRAY, (x + 2, y + 2), 17)
        
        # Main player circle
        pygame.draw.circle(screen, color, (x, y), 17)
        pygame.draw.circle(screen, BLACK, (x, y), 17, 2)
        
        # Player label with better visibility
        label = "M" if isinstance(player, MrX) else f"D{index}"
        font = pygame.font.Font(None, 28)  # Slightly larger font
        text = font.render(label, True, WHITE)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

def get_player_at_position(players, nodes_dict, pos):
    for player in players:
        node = nodes_dict.get(player.current_location())
        if node:
            x = int(node["position"]["x"] * scale_factor + offset_x)
            y = int(node["position"]["y"] * scale_factor + offset_y)
            if (x - pos[0]) ** 2 + (y - pos[1]) ** 2 <= 15 ** 2:
                return player
    return None

def get_node_at_position(nodes, pos):
    for node in nodes:
        x = int(node.get("position", {}).get("x", 0) * scale_factor + offset_x)
        y = int(node.get("position", {}).get("y", 0) * scale_factor + offset_y)
        if (x - pos[0]) ** 2 + (y - pos[1]) ** 2 <= 13 ** 2:
            return node
    return None

def show_game_over_popup(message):
    popup_width, popup_height = 300, 150
    popup_x = (WIDTH - popup_width) // 2
    popup_y = (HEIGHT - popup_height) // 2
    
    # Draw popup background
    pygame.draw.rect(screen, WHITE, (popup_x, popup_y, popup_width, popup_height))
    pygame.draw.rect(screen, BLACK, (popup_x, popup_y, popup_width, popup_height), 2)
    
    # Draw text
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over!", True, BLACK)
    message_text = font.render(message, True, BLACK)
    
    text_rect = text.get_rect(center=(WIDTH // 2, popup_y + 40))
    message_rect = message_text.get_rect(center=(WIDTH // 2, popup_y + 80))
    
    screen.blit(text, text_rect)
    screen.blit(message_text, message_rect)
    pygame.display.flip()
    
    # Wait for click or key press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN, pygame.QUIT):
                waiting = False
                return

def check_collision(mrx, detectives):
    for detective in detectives:
        if detective.current_node == mrx.current_node:
            show_game_over_popup("Detectives Win!")
            return True
    return False

def draw_ticket_info(player, font, position=(10, 50)):
    info_x, info_y = position
    bg_padding = 10

    if isinstance(player, MrX):
        tickets = [f"Black: {player.tickets.black}", f"Double: {player.tickets.double}"]
        color = RED
    else:
        tickets = [
            f"Taxi: {player.tickets.taxi}",
            f"Bus: {player.tickets.bus}", 
            f"Underground: {player.tickets.underground}"
        ]
        color = BLUE

    # Draw background
    max_width = max(font.size(text)[0] for text in tickets) + 2 * bg_padding
    total_height = len(tickets) * 25 + bg_padding
    pygame.draw.rect(screen, WHITE, (info_x - bg_padding, info_y - bg_padding, 
                                   max_width, total_height))
    pygame.draw.rect(screen, color, (info_x - bg_padding, info_y - bg_padding, 
                                   max_width, total_height), 2)

    # Draw ticket counts
    for i, text in enumerate(tickets):
        ticket_text = font.render(text, True, BLACK)
        screen.blit(ticket_text, (info_x, info_y + i * 25))

def draw_all_tickets(players, font, current_player):
    # Draw current player's tickets prominently
    draw_ticket_info(current_player, font, (10, 50))
    
    # Draw other players' tickets in a compact format
    y_offset = 150
    for i, player in enumerate(players):
        if player != current_player:
            if isinstance(player, MrX):
                tickets_text = f"MrX - B:{player.tickets.black} D:{player.tickets.double}"
            else:
                tickets_text = f"D{i} - T:{player.tickets.taxi} B:{player.tickets.bus} U:{player.tickets.underground}"
            text = font.render(tickets_text, True, BLACK)
            pygame.draw.rect(screen, WHITE, (5, y_offset, text.get_width() + 10, 25))
            screen.blit(text, (10, y_offset))
            y_offset += 30

def move_player(player, node, detectives, nodes_dict, use_black_ticket=False, use_double_ticket=False, double_ticket_first_move=False):
    if not isinstance(player, MrX):
        # Handle detective moves
        transport_type = player.get_valid_moves()[node["id"]]
        player.move_to_node(node["id"])
        player.use_ticket(transport_type)  # Subtract ticket
        return transport_type, False
    
    # Handle MrX moves
    if use_double_ticket:
        if double_ticket_first_move:
            # First move of double ticket
            player.use_ticket("double")
            return handle_double_ticket_move(player, node, detectives, nodes_dict, first_move=True)
        else:
            # Second move of double ticket
            return handle_double_ticket_move(player, node, detectives, nodes_dict, first_move=False)
    elif use_black_ticket:
        player.move_to_node(node["id"], detectives)
        player.use_ticket("black")
        return "black", False
    else:
        transport_type = player.get_valid_moves()[node["id"]]
        player.move_to_node(node["id"], detectives)
        player.use_ticket(transport_type)
        collision = any(detective.current_node == node["id"] for detective in detectives)
        return transport_type, collision

def draw_mrx_history(transport_history, font, position=None):
    """Draw MrX's movement history showing only transport types"""
    # Calculate position if not provided (right side of screen with padding)
    if position is None:
        padding = 20
        info_x = WIDTH - 250  # Fixed width from right side
        info_y = 100  # Start below the round counter
    else:
        info_x, info_y = position
    
    bg_padding = 10
    
    # Title
    title = "MrX Transport History:"
    title_text = font.render(title, True, BLACK)
    
    # Create transport type display strings
    history_texts = []
    for i, transport in enumerate(transport_history, 1):
        history_texts.append(f"Round {i}: {transport.upper()}")
    
    # Calculate background size
    max_width = max(
        max((font.size(text)[0] for text in history_texts), default=0),
        font.size(title)[0]
    ) + 2 * bg_padding
    
    # Ensure the panel doesn't go off screen
    if info_x + max_width > WIDTH - 10:
        info_x = WIDTH - max_width - 10
    
    total_height = (len(history_texts) + 1) * 25 + bg_padding
    
    # Draw background with semi-transparent effect
    background_surface = pygame.Surface((max_width + 2 * bg_padding, total_height + 2 * bg_padding))
    background_surface.fill(WHITE)
    background_surface.set_alpha(240)
    screen.blit(background_surface, (info_x - bg_padding, info_y - bg_padding))
    
    # Draw border
    pygame.draw.rect(screen, RED, 
                    (info_x - bg_padding, info_y - bg_padding, 
                     max_width + 2 * bg_padding, total_height + 2 * bg_padding), 2)
    
    # Draw title
    screen.blit(title_text, (info_x, info_y))
    
    # Draw history entries
    for i, text in enumerate(history_texts):
        history_text = font.render(text, True, BLACK)
        screen.blit(history_text, (info_x, info_y + (i + 1) * 25))

def show_black_ticket_popup():
    popup_width, popup_height = 300, 150
    popup_x = (WIDTH - popup_width) // 2
    popup_y = (HEIGHT - popup_height) // 2
    
    # Draw popup background
    pygame.draw.rect(screen, WHITE, (popup_x, popup_y, popup_width, popup_height))
    pygame.draw.rect(screen, BLACK, (popup_x, popup_y, popup_width, popup_height), 2)
    
    # Draw text
    font = pygame.font.Font(None, 36)
    text = font.render("Use Black Ticket?", True, BLACK)
    yes_text = font.render("Yes", True, BLACK)
    no_text = font.render("No", True, BLACK)
    
    text_rect = text.get_rect(center=(WIDTH // 2, popup_y + 40))
    yes_rect = yes_text.get_rect(center=(WIDTH // 2 - 50, popup_y + 100))
    no_rect = no_text.get_rect(center=(WIDTH // 2 + 50, popup_y + 100))
    
    screen.blit(text, text_rect)
    screen.blit(yes_text, yes_rect)
    screen.blit(no_text, no_rect)
    pygame.display.flip()
    
    # Wait for click or key press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_rect.collidepoint(event.pos):
                    return True
                elif no_rect.collidepoint(event.pos):
                    return False
            elif event.type in (pygame.KEYDOWN, pygame.QUIT):
                waiting = False
                return False

def show_double_ticket_popup():
    popup_width, popup_height = 300, 150
    popup_x = (WIDTH - popup_width) // 2
    popup_y = (HEIGHT - popup_height) // 2
    
    # Draw popup background
    pygame.draw.rect(screen, WHITE, (popup_x, popup_y, popup_width, popup_height))
    pygame.draw.rect(screen, BLACK, (popup_x, popup_y, popup_width, popup_height), 2)
    
    # Draw text
    font = pygame.font.Font(None, 36)
    text = font.render("Use Double Ticket?", True, BLACK)
    yes_text = font.render("Yes", True, BLACK)
    no_text = font.render("No", True, BLACK)
    
    text_rect = text.get_rect(center=(WIDTH // 2, popup_y + 40))
    yes_rect = yes_text.get_rect(center=(WIDTH // 2 - 50, popup_y + 100))
    no_rect = no_text.get_rect(center=(WIDTH // 2 + 50, popup_y + 100))
    
    screen.blit(text, text_rect)
    screen.blit(yes_text, yes_rect)
    screen.blit(no_text, no_rect)
    pygame.display.flip()
    
    # Wait for click or key press
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if yes_rect.collidepoint(event.pos):
                    return True
                elif no_rect.collidepoint(event.pos):
                    return False
            elif event.type in (pygame.KEYDOWN, pygame.QUIT):
                waiting = False
                return False

def handle_double_ticket_move(player, node, detectives, nodes_dict, first_move=True):
    """Handle a single move during double ticket usage"""
    use_black = False
    if player.tickets.black > 0:
        use_black = show_black_ticket_popup()
    
    transport_type = player.get_valid_moves()[node["id"]]
    
    if use_black:
        player.move_to_node(node["id"], detectives)
        player.use_ticket("black")
        return "black", False
    else:
        player.move_to_node(node["id"], detectives)
        player.use_ticket(transport_type)
        collision = any(detective.current_node == node["id"] for detective in detectives)
        return transport_type, collision

def main():
    global offset_x, offset_y, WIDTH, HEIGHT
    running = True
    dragging = False
    drag_start_x, drag_start_y = 0, 0
    needs_redraw = True
    selected_player = None
    highlighted_nodes = []
    use_black_ticket = False  # Initialize use_black_ticket
    use_double_ticket = False  # Initialize use_double_ticket
    double_ticket_first_move = False  # Track if it's the first move of a double ticket

    font = pygame.font.Font(None, 24)
    clock = pygame.time.Clock()

    # Convert nodes to a dictionary
    nodes = map if isinstance(game_map, list) else game_map.get("nodes", [])
    nodes_dict = {node["id"]: node for node in nodes}

    # Initialize game elements
    start, end = 1, 199
    exclude = {35, 45, 51, 71, 78, 104, 106, 127, 132, 146, 166, 170, 172}
    used_locations = set()

    # Create MrX instance first
    mrx = MrX.create(MrX_Tickets())
    mrx_spawn_location = mrx.current_location()  # Store initial spawn location
    
    detectives = [Detective(None, Detective_Tickets()) for _ in range(4)]
    for detective in detectives:
        detective.spawn(start, end, exclude, used_locations)

    players = [mrx] + detectives  # Move MrX to the end of the players list so turn order starts with MrX

    rounds = 0
    current_turn = 0  # Track which player's turn it is
    total_players = len(players)
    reveal_rounds = {3, 8, 13, 18, 24}

    # Add transport history tracking
    mrx_transport_history = []
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Exit fullscreen
                    pygame.display.set_mode((1400, 800), pygame.RESIZABLE)
                    handle_resize(1400, 800)
                    needs_redraw = True
                elif event.key == pygame.K_f:  # Toggle fullscreen
                    if screen.get_flags() & pygame.FULLSCREEN:
                        pygame.display.set_mode((1400, 800), pygame.RESIZABLE)
                        handle_resize(1400, 800)
                    else:
                        pygame.display.set_mode((infoObject.current_w, infoObject.current_h), 
                                              pygame.FULLSCREEN | pygame.RESIZABLE)
                        handle_resize(infoObject.current_w, infoObject.current_h)
                    needs_redraw = True
                elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    zoom(1.1)
                    needs_redraw = True
                elif event.key == pygame.K_MINUS:
                    zoom(0.9)
                    needs_redraw = True
            elif event.type == pygame.VIDEORESIZE:
                if not (screen.get_flags() & pygame.FULLSCREEN):
                    handle_resize(event.w, event.h)
                    needs_redraw = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    # Only allow clicking current player
                    current_player = players[current_turn]
                    clicked_player = get_player_at_position(players, nodes_dict, event.pos)
                    if clicked_player == current_player:
                        selected_player = clicked_player
                        highlighted_nodes = clicked_player.get_valid_moves().keys()
                        needs_redraw = True
                    else:
                        dragging = True
                        drag_start_x, drag_start_y = event.pos
                elif event.button == 3:  # Right click
                    current_player = players[current_turn]
                    clicked_player = get_player_at_position(players, nodes_dict, event.pos)
                    
                    if clicked_player == current_player and isinstance(clicked_player, MrX):
                        use_black_ticket = False
                        use_double_ticket = False
                        
                        # Ask for double ticket first
                        if clicked_player.tickets.double > 0:
                            use_double_ticket = show_double_ticket_popup()
                        
                        # If not using double ticket, ask for black ticket
                        if not use_double_ticket and clicked_player.tickets.black > 0:
                            use_black_ticket = show_black_ticket_popup()
                            
                        if use_black_ticket or use_double_ticket:
                            selected_player = clicked_player
                            highlighted_nodes = clicked_player.get_valid_moves().keys()
                            needs_redraw = True
                    
                    # ...continue with existing node click handling...
                    else:
                        node = get_node_at_position(nodes, event.pos)
                        if node and selected_player and node["id"] in highlighted_nodes:
                            transport_type, collision = move_player(
                                selected_player, node, detectives, nodes_dict,
                                use_black_ticket, use_double_ticket, double_ticket_first_move
                            )
                            
                            if isinstance(selected_player, MrX):
                                if use_double_ticket:
                                    if double_ticket_first_move:
                                        mrx_transport_history.append(f"DOUBLE: {transport_type}")
                                        double_ticket_first_move = False
                                    else:
                                        mrx_transport_history.append(transport_type)
                                        double_ticket_first_move = True
                                else:
                                    mrx_transport_history.append(transport_type)
                            
                            if collision:
                                show_game_over_popup("Detectives Win!")
                                running = False
                                break
                            
                            if use_double_ticket and double_ticket_first_move:
                                # Keep MrX selected for second move
                                highlighted_nodes = selected_player.get_valid_moves().keys()
                            else:
                                selected_player = None
                                highlighted_nodes = []
                                current_turn = (current_turn + 1) % total_players
                                if current_turn == 0:
                                    rounds += 1
                                    double_ticket_first_move = False
                            
                            needs_redraw = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if dragging:
                    dx, dy = event.pos[0] - drag_start_x, event.pos[1] - drag_start_y
                    offset_x = clamp(offset_x + dx, -(GRID_WIDTH * scale_factor), WIDTH)
                    offset_y = clamp(offset_y + dy, -(GRID_HEIGHT * scale_factor), HEIGHT)
                    drag_start_x, drag_start_y = event.pos
                    needs_redraw = True

        if needs_redraw:
            screen.fill(SILVER)
            
            # Get current window size
            current_width, current_height = screen.get_size()
            
            # Draw grid pattern that covers the entire window
            grid_size = 50
            for x in range(0, current_width + grid_size, grid_size):
                for y in range(0, current_height + grid_size, grid_size):
                    pygame.draw.rect(screen, (210, 210, 210), (x, y, grid_size, grid_size), 1)

            # Draw edges in layers: underground first, then bus, then taxi
            for node in nodes:
                draw_edges(node, nodes_dict, "underground")
            for node in nodes:
                draw_edges(node, nodes_dict, "bus")
            for node in nodes:
                draw_edges(node, nodes_dict, "taxi")

            # Draw nodes on top of all edges
            for node in nodes:
                is_mrx_move = selected_player and isinstance(selected_player, MrX)
                is_detective_move = selected_player and isinstance(selected_player, Detective)
                
                if is_mrx_move:
                    highlight_color = YELLOW
                elif is_detective_move:
                    highlight_color = GREEN
                else:
                    highlight_color = BLACK
                    
                draw_node(node, font, 
                         highlight=node["id"] in highlighted_nodes,
                         highlight_color=highlight_color)

            # Draw players
            if rounds == 0 or rounds in reveal_rounds:
                draw_player(mrx, nodes_dict, YELLOW if rounds == 0 else RED)
            for i, detective in enumerate(detectives, 1):
                draw_player(detective, nodes_dict, BLUE, i)

            # Update current player indicator
            current_player = players[current_turn]
            if isinstance(current_player, MrX):
                text = "MrX's turn"
                color = RED
            else:
                # Fix detective numbering - subtract 1 since current_turn starts at 1 for first detective
                detective_number = current_turn
                text = f"Detective {detective_number}'s turn"
                color = BLUE
            
            # Draw turn indicator with background
            font = pygame.font.Font(None, 32)
            turn_text = font.render(text, True, color)
            pygame.draw.rect(screen, WHITE, (5, 5, turn_text.get_width() + 20, 30))
            pygame.draw.rect(screen, BLACK, (5, 5, turn_text.get_width() + 20, 30), 2)
            screen.blit(turn_text, (15, 10))

            # Draw round counter
            round_text = font.render(f"Round: {rounds + 1}", True, BLACK)
            pygame.draw.rect(screen, WHITE, (WIDTH - round_text.get_width() - 25, 5, round_text.get_width() + 20, 30))
            pygame.draw.rect(screen, BLACK, (WIDTH - round_text.get_width() - 25, 5, round_text.get_width() + 20, 30), 2)
            screen.blit(round_text, (WIDTH - round_text.get_width() - 15, 10))

            # Draw current player's ticket info
            draw_all_tickets(players, font, current_player)

            # Draw MrX's transport history before pygame.display.flip()
            draw_mrx_history(mrx_transport_history, font)

            # Check if the current detective has valid moves
            current_player = players[current_turn]
            if isinstance(current_player, Detective) and not current_player.has_valid_moves():
                current_turn = (current_turn + 1) % total_players
                if current_turn == 0:  # All players have moved
                    rounds += 1
                needs_redraw = True
                continue

            # Check for collision after moves
            if check_collision(mrx, detectives):
                running = False
            
            # Check for MrX win condition
            if rounds >= 24:
                show_game_over_popup("MrX Wins!")
                running = False

            pygame.display.flip()
            needs_redraw = False

#        clock.tick(60)

if __name__ == "__main__":
    main()
