document.addEventListener('DOMContentLoaded', () => {
    const quizForm = document.getElementById('quiz-form');
    const quizSubmitButton = document.getElementById('quiz-submit');
    const certificateButton = document.querySelector('.certificate');
    const questions = document.querySelectorAll('.quiz-question');
    certificateButton.style.display = 'none';
    quizForm.addEventListener('change', () => {
        const allAnswered = [...questions].every(question => 
            question.querySelector('input[type="radio"]:checked')
        );
        quizSubmitButton.disabled = !allAnswered;
    });

    quizSubmitButton.addEventListener('click', () => {
        let correctCount = 0;
        questions.forEach(question => {
            const selectedAnswer = question.querySelector('input[type="radio"]:checked')?.value;
            const correctAnswer = question.getAttribute('data-correct-answer');
            const existingFeedback = question.querySelector('.feedback');
            if (existingFeedback) existingFeedback.remove();
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

        certificateButton.style.display = correctCount === questions.length ? 'block' : 'none';
    });
});
