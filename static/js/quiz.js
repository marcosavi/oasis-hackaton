document.addEventListener('DOMContentLoaded', () => {
    const quizForm = document.getElementById('quiz-form');
    const quizSubmitButton = document.getElementById('quiz-submit');
    const certificateButton = document.querySelector('.certificate');
    const questions = document.querySelectorAll('.quiz-question');

    // Initially hide the certificate button
    certificateButton.style.display = 'none';

    // Enable the submit button if all questions are answered
    quizForm.addEventListener('change', () => {
        const allAnswered = Array.from(questions).every(question => {
            return question.querySelector('input[type="radio"]:checked');
        });
        quizSubmitButton.disabled = !allAnswered;
    });

    quizSubmitButton.addEventListener('click', () => {
        let correctCount = 0;

        questions.forEach(question => {
            const selectedAnswer = question.querySelector('input[type="radio"]:checked')?.value;
            const correctAnswer = question.getAttribute('data-correct-answer');

            // Remove any existing feedback
            const existingFeedback = question.querySelector('.feedback');
            if (existingFeedback) {
                existingFeedback.remove();
            }

            // Create feedback span
            const feedback = document.createElement('span');
            feedback.classList.add('feedback');
            feedback.style.fontWeight = 'bold';

            if (selectedAnswer === correctAnswer) {
                correctCount++;
                feedback.style.color = 'green';
                question.style.backgroundColor = '#d4edda';
            } else {
                feedback.style.color = 'red';
                question.style.backgroundColor = '#f8d7da';
            }

            question.appendChild(feedback);
        });

        if (correctCount === questions.length) {
            certificateButton.style.display = 'block';
        } else {
            certificateButton.style.display = 'none';
        }
    });
});
