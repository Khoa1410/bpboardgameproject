let turn = 1;
const maxTurns = 10;
let questions = [];
let names = [];

function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

async function loadData() {
    const [questionsText, namesText] = await Promise.all([
        fetch('questions.txt').then(res => res.text()),
        fetch('names.txt').then(res => res.text())
    ]);
    questions = questionsText.split('\n').map(line => line.trim()).filter(line => line.length > 0);
    names = namesText.split('\n').map(line => line.trim()).filter(line => line.length > 0);
    shuffle(questions);
    shuffle(names);
}

async function getRandomEventAndName() {
    if (turn > maxTurns || questions.length === 0 || names.length === 0) {
        document.getElementById('question').innerText = "Đã hết lượt!";
        document.getElementById('name').innerText = "";
        document.getElementById('nextBtn').disabled = true;
        return;
    }
    const question = questions.pop();
    const name = names.pop();

    const questionDiv = document.getElementById('question');
    const nameDiv = document.getElementById('name');
    
    questionDiv.classList.remove('fade-in-turn');
    nameDiv.classList.remove('fade-in-turn');
    
    void questionDiv.offsetWidth;
    void nameDiv.offsetWidth;
    
    questionDiv.innerText = `Lượt ${turn}: ${question}`;
    nameDiv.innerText = `Người độc tài: ${name}`;
    
    questionDiv.classList.add('fade-in-turn');
    nameDiv.classList.add('fade-in-turn');

    turn++;
}

async function startGame() {
    await loadData();
    getRandomEventAndName();
    document.getElementById('nextBtn').addEventListener('click', getRandomEventAndName);
}


document.getElementById('startBtn').addEventListener('click', startGame);