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
                feedback.textContent = ' ✔ Correct';
                feedback.style.color = 'green';
                question.style.backgroundColor = '#d4edda'; // Green for correct
            } else {
                feedback.textContent = ' ✘ Incorrect';
                feedback.style.color = 'red';
                question.style.backgroundColor = '#f8d7da'; // Red for incorrect
            }

            // Append feedback to the question
            question.appendChild(feedback);
        });

        // Show or hide the certificate button based on correctness
        if (correctCount === questions.length) {
            certificateButton.style.display = 'block'; // Show the certificate button
        } else {
            certificateButton.style.display = 'none'; // Ensure the certificate button stays hidden
        }
    });
});
