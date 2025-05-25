let players = [];
let votes = [];


function generateNameInputs() {
    const num = parseInt(document.getElementById("numPlayers").value);
    const nameInputs = document.getElementById("nameInputs");
    nameInputs.innerHTML = "";

    for (let i = 0; i < num; i++) {
        const input = document.createElement("input");
        input.placeholder = `Player ${i + 1} name`;
        input.id = `player${i}`;
        nameInputs.appendChild(input);
        nameInputs.appendChild(document.createElement("br"));
    }
}


function startGame() {
    const num = parseInt(document.getElementById("numPlayers").value);
    players = [];

    for (let i = 0; i < num; i++) {
        const name = document.getElementById(`player${i}`).value.trim();
        if (name) players.push(name);
    }

    fetch('/start_game', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ players: players })
    }).then(() => {
        document.getElementById("setup").style.display = "none";
        document.getElementById("game").style.display = "block";
        nextTurn();
    });
}


function nextTurn() {
    fetch('/next_turn', { method: 'POST' })
        .then(res => res.json())
        .then(data => {
            document.getElementById("eventCard").innerText = data.card;
            document.getElementById("dictatorDisplay").innerText = "Dictator: " + data.dictator;
            players = data.players;
            generateVoteInputs(players);
        });
}


function generateVoteInputs(players) {
    const area = document.getElementById("voteArea");
    area.innerHTML = "";
    votes = [];

    players.forEach((p, i) => {
        const label = document.createElement("label");
        label.innerText = `${p} votes for: `;

        const select = document.createElement("select");
        select.dataset.index = i;

        players.forEach(name => {
            const option = document.createElement("option");
            option.value = name;
            option.text = name;
            select.appendChild(option);
        });

        area.appendChild(label);
        area.appendChild(select);
        area.appendChild(document.createElement("br"));
    });
}


function submitVotes() {
    const selects = document.querySelectorAll("select");
    let playerVotes = [];

    selects.forEach(s => {
        playerVotes.push(s.value);
    });


    const dictatorVote = playerVotes[0];

    fetch('/submit_vote', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            dictator_vote: dictatorVote,
            votes: playerVotes
        })
    }).then(res => res.json())
      .then(data => {
        const scoreList = document.getElementById("scoreList");
        scoreList.innerHTML = "";
        data.scores.forEach((score, idx) => {
            const li = document.createElement("li");
            li.innerText = `${players[idx]}: ${score} point(s)`;
            scoreList.appendChild(li);
        });
    });
}
