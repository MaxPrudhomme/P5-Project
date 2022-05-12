async function loadPlayerStats(userIdentifier)
{
    document.getElementById("playerSearchContainer").style.height = "40px";
    document.getElementById("playerOutputContainer").style.height = "0px";

    var response = await fetch("statsPlatform/json/" + userIdentifier.substring(1) + ".json");
    data = await response.json();
    
    //Player Stats
    document.getElementById("winrate").innerHTML = data.playerStats.winrate + " %";
    document.getElementById("wins").innerHTML = data.playerStats.wins + " games";
    document.getElementById("looses").innerHTML = data.playerStats.looses + " games";
    document.getElementById("draws").innerHTML = data.playerStats.draws + " games";
    //Game Stats
    document.getElementById("average").innerHTML = data.gameStats.average + " minutes";
    document.getElementById("fastest").innerHTML = data.gameStats.fastest + " minutes";
    document.getElementById("longest").innerHTML = data.gameStats.longest + " minutes";
    document.getElementById("winstreak").innerHTML = data.gameStats.winstreak + " games in a row";
    //User Info
    document.getElementById("username").innerHTML = data.username;
    document.getElementById("userID").innerHTML = "#" + data.userID;
    document.getElementById("firstConnection").innerHTML = data.firstConnection;
    document.getElementById("lastConnection").innerHTML = data.lastConnection;
}

async function playerSearcher()
{
    var userIdentifier = ""
    $.each($('#playerField').serializeArray(), function() {
        userIdentifier = this.value
    });

    if (userIdentifier.charAt(0) == "#")
    {
        loadPlayerStats(userIdentifier);
    }
    else
    {
    const users = await fetch("statsPlatform/json/users.json");
    const usersData = await users.json()
    var containerSize = 40;
    var outputContainer = document.getElementById("playerOutputContainer")

    var matchingUsers = {}

    for(key in usersData) { if(userIdentifier == usersData[key]) { matchingUsers[key] = userIdentifier[key]; }}

    if (Object.keys(matchingUsers).length == 1)
    {
        loadPlayerStats(Object.keys(matchingUsers)[0])
    }
    else
    {
        for (key in matchingUsers)
        {
            if (userIdentifier == usersData[key])
            {
                containerSize = containerSize + 40;
                var pattern = '<div class="playerResult" id="playerID" onclick="loadPlayerStats(this.id)"><span>playerName</span><span>playerID</span></div>'
                pattern = pattern.replace("playerName", usersData[key])
                pattern = pattern.replaceAll("playerID", key)
                outputContainer.insertAdjacentHTML("afterbegin", pattern)
            }
        }
        document.getElementById("playerSearchContainer").style.height = containerSize + "px";
        document.getElementById("playerOutputContainer").style.height = containerSize + "px";
        }
    }
}