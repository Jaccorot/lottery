$(document).ready(function()
	{
		var i=0,total=0
		total=$("tbody>tr>td").size()
		nodes=$("tbody>tr>td").get().reverse()

		for(i=0;i<total;i++)
		{	
/*			console.log(nodes[i].innerHtml);
			console.log(typeof(nodes[i].innerText));
			console.log(nodes[i].innerText);
			console.log(nodes[i].innerText.length)*/

			if (nodes[i].innerText.length ==0 ){
				nodes[i].innerText =1
			}
		}

/*			alert($(".analysis").eq(total).text());*/

/*		for(i=total;i!=0;i--)
		{
			alert($(".analysis:eq(i)").text())
	$(".analysis:empty").gt("107").text(1);
		}*/


	});