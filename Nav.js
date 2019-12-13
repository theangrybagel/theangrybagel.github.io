var links = [];
var titles = [];
var toRoot = "";

//used to get to the root directory
setTimeout(function(){ FixLinks()}, 10);
for(i = 0; i < DirectoryAmt; i++)
{
    toRoot += "../";
}
function AddLink(title, href) {
    
    var hrefB = toRoot;
    console.log(hrefB);
    hrefB += href;
    console.log(hrefB);
    links.push([title, hrefB]);
    titles.push(title);
}

var navCode = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css"> \
    <nav class="navbar navbar-expand-lg navbar-light bg-light background-light" style="border-radius: 0px"> \
        	<a class="navbar-brand navLink linkTheme" href="' + toRoot + 'index.html" target="_parent">WPLTS</a> \
        	<a class="navLink linkTheme" target="_parent" href="' + toRoot + 'index.html" title="Go to the homepage">Home</a> \
        	<a class="navLink linkTheme" href="#" onclick="random();" target="_parent" id="Random" title="Go to a random article">Random</a> \
        	<a class="searchPrompt" href="#" target="_parent" id="searchHref">Search</a> \
        <input type="text" class="searchBar" id="search00" onkeyup="Search()" placeholder="Search for something" title="Type to search"> \
    <span id="searched" class="background-light"></span> \
    </nav>';
    
function StartNav(){
AddLink('Home', './index.html');AddLink('', './Items/Supply.html');AddLink('', './Items/items.html');AddLink('', './Items/Weapons.html');AddLink('', './Items/Tools.html');AddLink('', './SpaceTerms/Fueltypes.html');AddLink('', './SpaceTerms/Shipterms.html');AddLink('', './SpaceTerms/Weaponclasses.html');AddLink('', './SpaceTerms/Terms.html');AddLink('', './SpaceTerms/Diseases.html');AddLink('Sectors', './Navigation/Sectors/Sectors.html');AddLink('Alpha Torgi', './Navigation/Sectors/Alpha Torgi/About.html');AddLink('', './Spaceships/Ships.html');AddLink('Eldons', './Races/Eldons.html');AddLink('Torgians', './Races/Torgians.html');AddLink('Eldons', './Races/Mateons.html');AddLink('', './Races/Races.html');
}
function random()
{
    var link = rand(0, links.length);
    OpenNew(links[link][1])
}
function FixLinks()
{
    var as = document.getElementsByTagName("a");
    for(i = 0; i < as.length; i++)
    {

        if(as[i].classList.contains('self') == false )
        {
            var href = as[i].getAttribute('href');
            var newHref = toRoot + href;
            as[i].setAttribute('href', newHref);
        }
        

    }
    
    as2 = document.getElementsByTagName("a");
    for(i = 0; i < as2.length; i++)
    {
        var newH = ""
        href = as2[i].getAttribute('href');
        console.log(href)
        console.log(href.split("/"))
        for(var ii = 0; ii < href.split("/").length; ii++)
        {
            slsh = "/"
            if(ii == 0) slsh = ""
            y = href.split("/")[ii]
            newH += slsh + y.trim()
        }
        as2[i].setAttribute("href", newH)
        console.log(document.getElementsByTagName("a")[i])
    }
}