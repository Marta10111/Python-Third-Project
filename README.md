# HORROR MOVIES QUIZ

<p>This project build in Python is a command line application. Users can check they knowledge of most known Horror Movies by answering 10 horror related questions. After each question they are informed do they answer is correct or not. Score they achieved is returned to them at the end of the quiz as well as option to play again if they want to improve they score.</P>

<a href="https://python-pp3.herokuapp.com/" aria_label="Link to deployed site">Link to deployed site</a>

![AmIResponsive](https://user-images.githubusercontent.com/106401395/194064596-821efe51-2849-4f15-bc2a-96180cb7a28b.jpg)

------

# Contents:

1. [Flowchart](#flowchart)
2. [Wireframe](#wireframe)
3. [User Experience](#user_experience)
4. [Features](#Features)
5. [Invalid Data Handling](#invalid-data-handling)
6. [Data Model](#data-model)
7. [Testing](#testing)
8. [Bugs](#bugs)
9. [Resources Used](#resources-used)
10. [Deployment](#deployment)
11. [Credits](#credits)

------

# Flowchart

I used <a href="https://www.lucid.app">Lucid</a> to create simple flowchart of how project should work from start to end. These helped me to visualise the structure of the code and which functions may be needed.

![FlowChart](https://user-images.githubusercontent.com/106401395/194067591-f76f183c-3b2c-4cb8-be59-4f03d0e8649d.jpg)

# Wireframe

I made a simple wireframe on a piece of paper including all 10 questions and answers. I've  also been told from one of my class student about ASCII convertor, thanks to her I create a quiz title using this app. 

# User Experience

## Project Goals
- Provide the User with a easy to play, multiple choice quiz.
- Provide some visuals with the use of colours to contribute to a positive user experience.
- Display the user’s score clearly at the end of the quiz.

## User Stories
As a User I want:
- To play easy to use quiz.
- Have clear instructions how to play.
- To test my knowledge of popular Horror Movies.
- To be informed when my input is invalid and what are the steps to correct it.
- To se whats my total score at the end of the quiz.
- To be easily repeat the quiz, if I want to play again or end it if I want to finish.

# Features

## Welcome screen
*Project Goal - Provide some visuals with images and colour to contribute to a positive user experience.*

I used ASCII font <a href="https://www.coolgenerator.com/ascii-text-generator">'ANSI Shadow'</a>, to create quiz title and Python module 'Colorama' to add color within the terminal.

The first input in the program asks the user to enter their name. This gives some personalisation to the quiz, as the program returns the name as a welcome.

![MainPage](https://user-images.githubusercontent.com/106401395/194073717-5793d777-6016-44f6-815a-2d5a0a063edf.jpg)

## Instructions
*Provide clear instructions on how to use the quiz.*

After the user has entered their Name, they are given a personalised welcome message, and are presented with a short description and simple instructions for the quiz.

![Instructions](https://user-images.githubusercontent.com/106401395/194075123-7aa654b7-fa56-46cb-a37e-cc4bce5cd4ec.jpg)

User is then asked if they are ready to start the quiz by typing 'y' for yes or 'n' for no. This allows User initiation and control of the logic flow in this stage of the program. If the User types 'y' the quiz will begin and if 'n' is typed a message will appear asking them to type 'y' when ready, and the question repeats.

![Not Ready to begin](https://user-images.githubusercontent.com/106401395/194075999-e0acee5c-fba6-4ebc-99f3-160c0e38127c.jpg)

## Questions
*Project Goal - provide the User with easy to play multiple choice quiz, where they can test thair knowledge of Horror Movies*

The quiz contains 10 multiple choice questions of, which are iterated through in the same order each time the program is run. Each correctly answered question scores 1 point, and if the question is answered incorrectly then 0 points are awarded. To improve readability I have coloured the questions blue, and used the 'style.bright' Colorama feature to add boldness to the text.

![Question](https://user-images.githubusercontent.com/106401395/194077335-db7711d4-dc36-42db-b2ed-73fbe162bae8.jpg)

If the correct answer is selected by the user, they are informed with the output 'You're right' which is colored in green, followed by the next question. If an incorrect answer is selected, the output 'You're wrong' is shown in red. 

![answer correct](https://user-images.githubusercontent.com/106401395/194078087-52857f59-e4dc-4ef8-b282-1db895b20ec0.jpg)

![Answer incorrect](https://user-images.githubusercontent.com/106401395/194078163-e23c1b77-bc2c-4165-956e-09fc8fe949ef.jpg)

## Final Score and Play Again
*Project Goal - display the user’s score clearly at the end of the quiz*
*Ask User If they want to repeat the game*

Once all 10 questions have been iterated through, the user is then presented with their final score. Different messages are displayed, depending on whether the score is equal to or less than 6, or greater than 6. The message is personalised with the users Name.

![good score](https://user-images.githubusercontent.com/106401395/194078944-72bf6f5e-f8c1-472b-8262-2bf89e33e71a.jpg)

![bad score](https://user-images.githubusercontent.com/106401395/194079006-43bba964-ec85-413b-8f21-e0659b3219ee.jpg)

The user is also asked if they would like to play again, by typing 'y' for yes or 'n' for no. If 'y' is typed the program sequence starts again. If 'n' is typed, a message informs the user that the quiz has ended and to click the 'Run Program' button if they wish to reset the quiz. 

![play again no](https://user-images.githubusercontent.com/106401395/194079572-ca27a36a-9b9d-4de4-b345-3acef1d37ac7.jpg)

# Invalid Data Handling

##Lower or Upper case characters
All input will be accepted in lower or upper case as long as the inserted input is allowed.

![Capital letter](https://user-images.githubusercontent.com/106401395/194080355-27f8a483-7418-455c-aa6c-778780e9ded6.jpg)

## Name Input
Users must enter a string of text in the Name input before they can proceed. If the input is left blank, or contains just whitespace, then an error message is displayed and the input is requested again.

![enter name](https://user-images.githubusercontent.com/106401395/194080696-370af756-0e86-4201-a7dc-fd5ada754722.jpg)

## Start Quiz
Users must type 'y' or 'n' to indicate if they are ready to start the quiz. If they enter any other character an error message is displayed and the input is requested again. 

![correct y or n](https://user-images.githubusercontent.com/106401395/194081060-482b3d8e-32b7-411b-aba1-8f65dc271bdf.jpg)

## Answer Input
Users must type 'a', 'b', 'c' or 'd' to select their chosen answer. If they enter any other character an error message is displayed and the question will be repeated. An invalid answer like this does not effect the users end score.

![answer input](https://user-images.githubusercontent.com/106401395/194081529-db5478af-1cb3-45c0-aa62-de43717fa2cd.jpg)

## Play Again
Users must type 'y' or 'n' to indicate whether or not they wish to play again. If they enter any other character an error message is displayed and the input is requested again.

![play again](https://user-images.githubusercontent.com/106401395/194081932-9533dda8-50b7-4d83-8adb-91e196031ab1.jpg)

# Data Model
In these program dictionary was used to store quiz questions and answers. That will help add more questions in the future without amend any code. This has been achieved by the use of f-Strings in print statements, so that accurate data is always displayed for the user score.

# Testing

## Manyal Testing












