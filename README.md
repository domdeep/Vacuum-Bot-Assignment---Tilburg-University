# **Vacuum Bot Assignment - Tilburg University**

This repository contains all the final files from my submission for the Vacuum Bot Logic Assignment, completed in **December 2013**. It includes Python code and a report discussing the methodologies and results. This project achieved an **8.5** grade and was part of the **Programming & Algorithm Thinking (Fall)** course, course number **822206-B-6**.

## **Project Overview**

This individual assignment involved designing and testing a bot, **noStainNoGain**, which cleans stains on a map by following specific movement logic. The bot prioritizes cleaning stains in vision and avoids obstacles while traversing the map from top to bottom, left to right.

## **Logic and Strategy**:

- **Priority Logic**: Clean stains immediately if in vision; move around obstacles when encountered.
- **Movement Pattern**: Moves rightwards on even rows and leftwards on odd rows.
- **Challenge**: The bot is unable to backtrack when it reaches dead ends on complex maps (10-grade).

## **Achievements**:

- Successfully tested the bot on **50 maps**, including **6-grade**, **7-grade**, **8-grade**, and **9-grade** maps, with an energy performance of **0.76** for 6 and 7-grade, and **0.56** for 9-grade maps.
- Performance consistently **outperformed BruteBot**, a competitor in all tested cases.
- The bot was unable to solve **10-grade** labyrinth maps due to the lack of backtracking functionality but excelled on simpler maps (6 to 9-grade).
- Iteratively improved the bot’s logic, though some potential enhancements were not fully implemented due to time constraints.

## **Project Structure**

- **Code**: Python code to implement and test the bot's logic.
- **Report**: A detailed report discussing the bot's logic, performance on generated maps, and potential improvements, such as implementing backtracking for solving more complex labyrinth maps.

