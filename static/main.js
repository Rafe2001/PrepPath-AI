async function askQuestion() {
    const questionInput = document.getElementById('questionInput');
    const question = questionInput.value.trim();

    if (!question) return;

    const response = await fetch('/ask', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question })
    });

    const result = await response.json();

    const messages = document.getElementById('messages');

    const questionDiv = document.createElement('div');
    questionDiv.className = 'message question';
    questionDiv.textContent = `Q: ${question}`;

    const answerDiv = document.createElement('div');
    answerDiv.className = 'message answer';
    answerDiv.textContent = `A: ${result.answer}`;

    messages.appendChild(questionDiv);
    messages.appendChild(answerDiv);
    questionInput.value = '';
    messages.scrollTop = messages.scrollHeight;
}
