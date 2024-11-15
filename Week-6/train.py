import pygame
from game_board import GameBoard
from player import Player
from rl_ai import RLAgent
import matplotlib.pyplot as plt

def plot_rewards(rewards1, rewards2):
    plt.figure(figsize=(10, 5))
    plt.plot(rewards1, label='Player 1')
    plt.plot(rewards2, label='Player 2')
    plt.title('Episode Rewards over Time')
    plt.xlabel('Episode')
    plt.ylabel('Total Reward')
    plt.legend()
    plt.savefig('rewards_plot.png')
    plt.close()

def plot_steps(steps):
    plt.figure(figsize=(10, 5))
    plt.plot(steps)
    plt.title('Steps Survived over Time')
    plt.xlabel('Episode')
    plt.ylabel('Steps')
    plt.savefig('steps_plot.png')
    plt.close()

def train():
    game_board = GameBoard(40, 30)
    rl_agent1 = RLAgent(state_size=7*7*3, action_size=4, player_id=1)
    rl_agent2 = RLAgent(state_size=7*7*3, action_size=4, player_id=2)
    player1 = Player(10, 15, (255, 0, 0), 1, rl_agent1)
    player2 = Player(30, 15, (0, 0, 255), 2, rl_agent2)
    
    # Set opponents
    player1.set_opponent(player2)
    player2.set_opponent(player1)

    num_episodes = 1000

    rewards1 = []
    rewards2 = []

    all_steps = []

    for episode in range(num_episodes):
        game_board = GameBoard(40, 30)
        player1.reset(10, 15)
        player2.reset(30, 15)
        
        done = False
        
        total_reward1 = 0
        total_reward2 = 0

        while not done:
            # Player 1's turn
            player1.move(game_board)

            # Player 2's turn
            player2.move(game_board)

            player1Collision = game_board.is_collision(player1.x, player1.y)
            player2Collision = game_board.is_collision(player2.x, player2.y)

            # Check for collisions
            if player1Collision:
                #print(f"Player 1 collided at ({player1.x}, {player1.y})")
                
                if(player1Collision == 1):
                    reward1, reward2 = -10, 10
                else:
                    reward1, reward2 = -10, 10

                done = True
            elif player2Collision:
                #print(f"Player 2 collided at ({player2.x}, {player2.y})")

                if(player1Collision == 1):
                    reward1, reward2 = 10, -10
                else:
                    reward1, reward2 = 10, -10
                
                done = True
            else:
                reward1, reward2 = 1, 1  # Small reward for surviving

            total_reward1 += reward1
            total_reward2 += reward2

            # Update game board
            if not done:
                game_board.grid[player1.y][player1.x] = player1.player_id
                game_board.grid[player2.y][player2.x] = player2.player_id

            # Get new states
            next_state1 = rl_agent1.get_state(game_board, player1, player2)
            next_state2 = rl_agent2.get_state(game_board, player2, player1)

            # Remember the transitions
            rl_agent1.remember(rl_agent1.get_state(game_board, player1, player2), player1.direction, reward1, next_state1, done)
            rl_agent2.remember(rl_agent2.get_state(game_board, player2, player1), player2.direction, reward2, next_state2, done)

            # Train the agents
            rl_agent1.replay(32)
            rl_agent2.replay(32)

        rewards1.append(total_reward1)
        rewards2.append(total_reward2)

        if episode % 10 == 0:
            print(f"Episode: {episode}, Player 1 Reward: {total_reward1}, Player 2 Reward: {total_reward2}")

        if episode % 100 == 0:
            print(f"Episode: {episode}, Player 1 Reward: {total_reward1}, Player 2 Reward: {total_reward2}")
            plot_rewards(rewards1, rewards2)

    rl_agent1.save_model("tron_model_player1.pth")
    rl_agent2.save_model("tron_model_player2.pth")
    plot_rewards(rewards1, rewards2)

if __name__ == "__main__":
    train()