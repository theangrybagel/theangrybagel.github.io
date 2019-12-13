setTimeout(function(){AddNavbar();}, 10);
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



