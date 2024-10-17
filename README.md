# **Vacuum Bot Assignment - Tilburg University**

This repository contains all the final files from my submission for the Vacuum Bot Logic Assignment, completed in **December 2013**. It includes Python code and a report discussing the methodologies and results. This project achieved an **8.5** grade and was part of the **Programming & Algorithm Thinking (Fall)** (**822206-B-6**) course.

## **Project Overview**

This individual assignment involved designing and testing a bot, **noStainNoGain**, which cleans stains on a map by following specific movement logic. The bot prioritizes cleaning stains in vision and avoids obstacles while traversing the map from top to bottom, left to right.

## **Logic and Strategy**:

- **Priority Logic**: Clean stains immediately if in vision; move around obstacles when encountered.
- **Movement Pattern**: Moves rightwards on even rows and leftwards on odd rows.
- **Challenge**: The bot is unable to backtrack when it reaches dead ends on complex maps (10-grade).

## **Achievements**:

- Successfully solved maps up to **9-grade**.
- Performance exceeds or equals that of **BruteBot** in all tested cases.
- Improvements in performance on simpler maps (**6 to 9-grade**).

## **Project Structure**

- **Code**: Python code to implement and test the bot's logic.
- **Report**: A detailed report discussing the bot's logic, performance on generated maps, and potential improvements, such as implementing backtracking for solving more complex labyrinth maps.

