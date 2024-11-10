let flashcards = [];
let currentSlide = 0;

function add_flashcard() {
    const question = document.getElementById('question').value;
    const answer = document.getElementById('answer').value;

    if (question && answer) {
        const flashcard = {
            question: question,
            answer: answer
        };

        flashcards.push(flashcard); 
        displayFlashcards();          
        clearForm();                 
    } else {
        alert('Please enter both question and answer.');
    }
}

function hide_flashcard() {
    if (flashcards.length > 0) {
        flashcards.pop();             
        displayFlashcards();          
    } else {
        alert('No flashcards to remove.');
    }
}

function displayFlashcards() {
    const container = document.getElementById('flashcards-container');
    container.innerHTML = '';        

    flashcards.forEach((flashcard, index) => {
        const flashcardElement = document.createElement('div');
        flashcardElement.classList.add('flashcard');

        const flashcardInner = document.createElement('div');
        flashcardInner.classList.add('flashcard-inner');

        const front = document.createElement('div');
        front.classList.add('front');
        front.textContent = flashcard.question;

        const back = document.createElement('div');
        back.classList.add('back');
        back.textContent = flashcard.answer;

        flashcardInner.appendChild(front);
        flashcardInner.appendChild(back);
        flashcardElement.appendChild(flashcardInner);

        
        if (index === currentSlide) {
            flashcardElement.style.display = 'flex';
        } else {
            flashcardElement.style.display = 'none';
        }

        container.appendChild(flashcardElement);
    });
}

function moveSlide(direction) {
    if (flashcards.length === 0) {
        alert('No flashcards available.');
        return;
    }

    currentSlide += direction;
    if (currentSlide < 0) currentSlide = flashcards.length - 1;
    if (currentSlide >= flashcards.length) currentSlide = 0;

    displayFlashcards();
}

function clearForm() {
    document.getElementById('question').value = '';
    document.getElementById('answer').value = '';
}

function returnToMain() {
    window.location.href = 'index.html'; // Add the link to the main page.
}