setTimeout(function(){AddNavbar();}, 10);
setTimeout(function(){ApplySpoilers();}, 100);
//setInterval(SpoilerUpdate, 10)

String.prototype.replaceAt = function(index, replacement) {
    return this.substr(0, index) + replacement + this.substr(index + replacement.length);
}
var spoilerData = {};
var currentlyTargetedSpoilers = [];
/*
function SpoilerUpdate()
{
    currentlyTargetedSpoilers.forEach(function(e)
    {
        indexOfChosenIndex = rand(0, e.indexes.length);
        chosenIndex = e.indexes[indexOfChosenIndex];
        newTxt = e.spoiler.innerHTML;
        var changeToReal = rand(0, 10) < 9;
        if(changeToReal)
        {
            newTxt = newTxt.replaceAt(chosenIndex, e.targetTxt[chosenIndex]);
            e.indexes.splice(indexOfChosenIndex, 1);
        }
        else{

        }
        e.spoiler.innerHTML = newTxt;
    });
}*/
function getE(elementName)
{
    return document.getElementById(elementName);
}
function rand(min, max)
{
    return Math.floor(Math.random() * (max - min) + min);
}
function OpenNew(location)
{
    window.open(location);
}
function AddElement(ename)
{
    var para = document.createElement("p");
    para.setAttribute("id", ename);
var node = document.createTextNode("This is new.");
para.appendChild(node);

var element = document.getElementsByTagName('head')[0];
element.appendChild(para);
}

function RandLetter()
{
    arr = "abcdefghijklmnopqrstuvwxyz1234567890"
    return arr[rand(0, arr.length)]
}

function RevealSpoiler(id)
{
    //console.location("Reveal " + id);
    var spoiler = document.getElementById(id);
    if(spoiler == null) return;
    var targetTxt = spoilerData[id];
    var indexes = [];
    spoiler.innerHTML = targetTxt;
    for(var i = 0; i < targetTxt.length; i+=1)
    {
        indexes.push(i);
    }
    newSpoiler = {spoiler: spoiler, targetTxt: targetTxt, indexes: indexes}
    currentlyTargetedSpoilers.push(newSpoiler);
    /*
    while(indexes.length > 0)
    {

        
        console.log(newTxt);
    }*/
}
function HideSpoiler(id)
{
    var spoiler = document.getElementById(id);
    if(spoiler == null) return;
    n = "";

    var inTag = false
    spoiler.innerHTML.split("").forEach(function(letter)
    {
        if(letter == "<")
            inTag = true;
        if(letter == ">")
            inTag = false;
        if([" ", "<", ">", ",", "."].includes(letter) || inTag)
        {
            n += letter;
        }
        else{
            n += RandLetter();
        }

    });
    spoiler.innerHTML = n;
}
function ApplySpoilers()
{
    spoilers = document.getElementsByClassName("spoilers");
    document.querySelectorAll('.edit').forEach(function(button) {
    // Now do something with my button
});
    var index = -1;
    document.querySelectorAll(".spoilers").forEach(function(spoiler){
        index += 1;
        console.log(spoiler)
        spoiler.id = "spoiler" + index;
        spoilerData[spoiler.id] = spoiler.innerHTML;
        spoiler.setAttribute("onmouseenter", "RevealSpoiler('spoiler" + index+"')")
        spoiler.setAttribute("onmouseleave", "HideSpoiler('spoiler" + index+"')")
        HideSpoiler(spoiler.id);
    });
}
function Search() {
        var result = "";
        var searchTxt = getE("search00").value.toLowerCase();
        //var pos = getPosition(getE("search00"));
        var results = 0;
        //console.log(pos);
        var txtValue;
        var filter = searchTxt.toLowerCase();
        for (i = 0; i < titles.length; i++) {
            td = titles[i];
            if (td) {
                txtValue = td || td;
                if (txtValue.toLowerCase().indexOf(filter) > -1) {
                    if(results < 6)
                    {
                        results += 1;
                        if(result > 1)
                        result += " | ";
                    result += "<a href='" + links[i][1] + "' title='" + links[i][1] + "'>" +  td + "</a>";
                    
                    }
                }
            }
        }
        if (searchTxt == "")
            result = "";
        document.getElementById("searched").innerHTML = result;
        //var posStyle = ("position: absolute; top:" + (pos[0] + 40) + "px; left: " + pos[1] + "px; ");
        //console.log(posStyle);
        //getE("searched").style = posStyle;
    }
function AddNavbar()
{
    getE("NavBarThing").innerHTML = navCode;
}
function getPosition(el)
{
    
    var rect = el.getBoundingClientRect(),
    scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,
    scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    return [rect.top + scrollTop, rect.left + scrollLeft];
}



