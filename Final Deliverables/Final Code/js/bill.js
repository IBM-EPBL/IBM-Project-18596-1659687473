function checkvalid()
{
	var nm=document.forms["bil"]["cnma"].value;
	var mo=document.forms["bil"]["mob"].value;
	var ph=/^\d{10}$/;
		if(nm,mo=="")
		{
			alert("Please enter customer name and mobile no");
		}
		else if(!isNaN(nm))
		{
			alert("Please enter correct input");
		}
		else if(!mo.match(ph))
		{
			alert("Please enter only 10 digit in moblie no");
		}
}
function calc_sale()
{
var s=document.forms["bil"]["qty1"].value;
var a=document.forms["bil"]["mrp1"].value;
var l=document.forms["bil"]["disc1"].value;
l = (l / 100)* a;//convert % to decimal
var fp=s * (a - l);
document.forms["bil"]["sp1"].value=fp;

var x=document.forms["bil"]["qty2"].value;
var y=document.forms["bil"]["mrp2"].value;
var z=document.forms["bil"]["disc2"].value;
z= (z / 100)* y;
var p=x * (y - z);
document.forms["bil"]["sp2"].value=p;

var e=document.forms["bil"]["qty3"].value;
var f=document.forms["bil"]["mrp3"].value;
var g=document.forms["bil"]["disc3"].value;
g= (g / 100)* f;
var b=e * (f - g);
document.forms["bil"]["sp3"].value=b;

var q=document.forms["bil"]["qty4"].value;
var m=document.forms["bil"]["mrp4"].value;
var d=document.forms["bil"]["disc4"].value;
d= (d/100)* m;
var w=q * (m - d);
document.forms["bil"]["sp4"].value=w;
}
function final_price()
{
var price1=document.forms["bil"]["sp1"].value;
var price2=document.forms["bil"]["sp2"].value;
var price3=document.forms["bil"]["sp3"].value;
var price4=document.forms["bil"]["sp4"].value;
var finalprice=+price1 + +price2 + +price3 + +price4;
document.forms["bil"]["t"].value=finalprice;
}