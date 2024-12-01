document.addEventListener('DOMContentLoaded', () => {
    const quizForm = document.getElementById('quiz-form');
    const quizSubmitButton = document.getElementById('quiz-submit');
    const certificateForm = document.getElementById('certificate-form');

    quizForm.addEventListener('change', () => {
        quizSubmitButton.disabled = false;
    });

    quizSubmitButton.addEventListener('click', () => {
        const selectedAnswer = document.querySelector('input[name="quiz-answer"]:checked').value;
        if (selectedAnswer === 'b') { // Correct answer validation
            alert("Correct answer! You can now claim your certificate.");
            certificateForm.style.display = 'block'; // Show the certificate form
        } else {
            alert("Incorrect answer. Please try again.");
        }
    });
});
