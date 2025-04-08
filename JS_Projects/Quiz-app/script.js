document.addEventListener('DOMContentLoaded', () => {
    const quizData = [
        {
            question: "Which keyword is used to declare variables in JavaScript?",
            options: ["var", "let", "const", "All of the above"],
            answer: "All of the above"
        },
        {
            question: "What does 'DOM' stand for in JavaScript?",
            options: [
                "Document Object Model",
                "Data Object Management",
                "Digital Orientation Method",
                "Display Object Manipulation"
            ],
            answer: "Document Object Model"
        },
        {
            question: "Which method converts JSON to a JavaScript object?",
            options: [
                "JSON.parse()",
                "JSON.stringify()",
                "JSON.convert()",
                "JSON.toObject()"
            ],
            answer: "JSON.parse()"
        },
        {
            question: "What is the output of: console.log(typeof [])?",
            options: ["array", "object", "undefined", "string"],
            answer: "object"
        },
        {
            question: "Which of these is NOT a JavaScript framework?",
            options: ["React", "Angular", "Vue", "Flask"],
            answer: "Flask"
        }
    ];

    const questionElement = document.getElementById('question');
    const optionsContainer = document.getElementById('options');
    const nextButton = document.getElementById('next-btn');
    const questionCounter = document.getElementById('question-counter');
    const scoreElement = document.getElementById('score');
    const resultElement = document.getElementById('result');

    let currentQuestionIndex = 0;
    let score = 0;
    let selectedOption = null;
    let quizCompleted = false;

    function loadQuestion() {
        const currentQuestion = quizData[currentQuestionIndex];
        questionElement.textContent = currentQuestion.question;
        
        optionsContainer.innerHTML = '';
        currentQuestion.options.forEach(option => {
            const optionElement = document.createElement('div');
            optionElement.classList.add('option');
            optionElement.textContent = option;
            optionElement.addEventListener('click', () => selectOption(optionElement, option));
            optionsContainer.appendChild(optionElement);
        });

        questionCounter.textContent = `Question ${currentQuestionIndex + 1}/${quizData.length}`;
        scoreElement.textContent = `Score: ${score}`;
        nextButton.disabled = true;
        selectedOption = null;
    }

    function selectOption(optionElement, option) {
        if (quizCompleted) return;

        // Remove selected class from all options
        document.querySelectorAll('.option').forEach(opt => {
            opt.classList.remove('selected');
        });

        // Add selected class to clicked option
        optionElement.classList.add('selected');
        selectedOption = option;
        nextButton.disabled = false;
    }

    function checkAnswer() {
        if (selectedOption === null) return;

        const currentQuestion = quizData[currentQuestionIndex];
        const options = document.querySelectorAll('.option');

        options.forEach(option => {
            option.classList.remove('correct', 'incorrect');
            if (option.textContent === currentQuestion.answer) {
                option.classList.add('correct');
            } else if (option.textContent === selectedOption && selectedOption !== currentQuestion.answer) {
                option.classList.add('incorrect');
            }
            option.style.cursor = 'default';
        });

        if (selectedOption === currentQuestion.answer) {
            score++;
            scoreElement.textContent = `Score: ${score}`;
        }

        nextButton.textContent = currentQuestionIndex === quizData.length - 1 ? 'Show Results' : 'Next Question';
        quizCompleted = true;
    }

    function showNextQuestion() {
        if (!quizCompleted && selectedOption !== null) {
            checkAnswer();
            return;
        }

        currentQuestionIndex++;
        if (currentQuestionIndex < quizData.length) {
            quizCompleted = false;
            loadQuestion();
            nextButton.textContent = 'Next Question';
        } else {
            showResult();
        }
    }

    function showResult() {
        questionElement.textContent = '';
        optionsContainer.innerHTML = '';
        nextButton.classList.add('hidden');
        
        const percentage = Math.round((score / quizData.length) * 100);
        let message;
        
        if (percentage >= 80) {
            message = `Excellent! You scored ${score}/${quizData.length} (${percentage}%)`;
        } else if (percentage >= 60) {
            message = `Good job! You scored ${score}/${quizData.length} (${percentage}%)`;
        } else {
            message = `Keep practicing! You scored ${score}/${quizData.length} (${percentage}%)`;
        }
        
        resultElement.textContent = message;
        resultElement.classList.remove('hidden');
    }

    nextButton.addEventListener('click', showNextQuestion);
    loadQuestion();
});
