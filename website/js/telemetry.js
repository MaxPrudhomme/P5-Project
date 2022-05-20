var updating = true

async function update()
{
    var response = await fetch("telemetryPlatform/json/activeGame.json");
    data = await response.json();

    document.getElementById("player1").innerHTML = data.player1
    document.getElementById("player2").innerHTML = data.player2

    game = data.currentState.game

    if ((Date.now() - data.lastInteraction) / 60000 < 5)
    {
        gameStatus = document.getElementById("status")
        gameStatus.innerHTML = "Playing"
        gameStatus.style.borderColor = "green"
        gameStatus.style.backgroundColor = "#1d8c19"

        document.getElementById("move").innerHTML = "Last Move : " + data.currentState.move
        document.getElementById("duration").innerHTML = "Turn Duration : " + data.currentState.duration + " s"
        for (let spot = 1; spot < 15; spot++)
        {
            document.getElementById(spot).innerHTML = game[spot]
        }
        document.getElementById(data.currentState.move).style.borderColor = "green"
    }
    if (updating == true)
    {
        setTimeout(update, 2000)
    }
}

function stopUpdate()
{
    updating = false
}

function startUpdate()
{
    updating = true
    update()
}