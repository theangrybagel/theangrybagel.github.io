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
AddLink('Locations', './Locations.html');AddLink('Home', './index.html');AddLink('NPC Creation', './RPGMechanics/NPCCreation.html');AddLink('Movement', './RPGMechanics/Movement.html');AddLink('Misc', './RPGMechanics/Misc.html');AddLink('Character Sheet', './RPGMechanics/CharacterSheet.html');AddLink('Classes', './RPGMechanics/Classes.html');AddLink('Combat', './RPGMechanics/Combat.html');AddLink('Character Creation', './RPGMechanics/CharacterCreation.html');AddLink('Encounters', './RPGMechanics/Encounters.html');AddLink('RPG Mechanics', './RPGMechanics/RPGMechanics.html');AddLink('Materials', './Items/Supply.html');AddLink('Items', './Items/items.html');AddLink('Weapons', './Items/Weapons.html');AddLink('Items and Vehicles', './Items/ItemsAndShips.html');AddLink('Tools', './Items/Tools.html');AddLink('Armor', './Items/Armor.html');AddLink('Vehicles', './Items/Vehicles.html');AddLink('Tools', './Items/Food.html');AddLink('The Concept Of Space Travel', './Books/ConceptSpaceTravel.html');AddLink('Campaigns', './Campaigns/Campaigns.html');AddLink('1', './Campaigns/1.html');AddLink('Map', './SectorMap/Sectors.html');AddLink('Map', './SectorMap/Sector 71/KFP-48-Etis-FBF-11-Dainerth Delta II/Linzioclite Iota X/CommonPlace.html');AddLink('Fuel Types', './SpaceTerms/Fueltypes.html');AddLink('Ship Terms', './SpaceTerms/Shipterms.html');AddLink('Weapons', './SpaceTerms/untitled.html');AddLink('Aliens', './SpaceTerms/Aliens.html');AddLink('Organizations', './SpaceTerms/Groups.html');AddLink('Books', './SpaceTerms/Books.html');AddLink('Weapon Classes', './SpaceTerms/Weaponclasses.html');AddLink('Terms', './SpaceTerms/Terms.html');AddLink('Diseases', './SpaceTerms/Diseases.html');AddLink('WPTLS - Sectors', './Navigation/Sectors/Sectors.html');AddLink('Spaceships', './Spaceships/Ships.html');AddLink('Shop Generator', './Generators/ShopGenerator.html');AddLink('NPC Generator', './Generators/NPCGenerator.html');AddLink('Generators', './Generators/Generators.html');AddLink('Matelons', './Races/Matelons.html');AddLink('Eldons', './Races/Eldons.html');AddLink('Grolotunians', './Races/Grolotunians.html');AddLink('Torgians', './Races/Torgians.html');AddLink('Galaians', './Races/Galaians.html');AddLink('Photonians', './Races/Photonians.html');AddLink('Races', './Races/Races.html');
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