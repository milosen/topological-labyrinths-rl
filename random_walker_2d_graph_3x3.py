import os

import gym

import topological_labyrinths_rl


if __name__ == '__main__':
    mazes_file = os.path.join("mazes", "mazes_3x3_54AB0B86.p")
    env = gym.make("topological-labyrinths-2D-v0")
    obs = env.reset()
    print(obs)
    done = False
    sum_reward = 0
    while not done:
        action = env.action_space.sample()
        state, reward, done, _ = env.step(action)
        sum_reward += reward
        env.render()
    print(f"Episode is over! You got {round(sum_reward, 2)} score.")
