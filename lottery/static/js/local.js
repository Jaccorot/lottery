$(function(){
   var nodes=$("tbody>tr").get().reverse();
    $.each(nodes,function(k,v){
    	//判断本次开奖号码的类型
	   	if(($(this).find(".td_num1").text() == $(this).find(".td_num2").text()) && ($(this).find(".td_num1").text() == $(this).find(".td_num3").text())){
	    		$(this).find(".baozi").text("豹子").addClass("analysis").removeClass("interval");
	    	}else if(($(this).find(".td_num1").text() != $(this).find(".td_num2").text()) && ($(this).find(".td_num1").text() != $(this).find(".td_num3").text()) && ($(this).find(".td_num2").text() != $(this).find(".td_num3").text())){
	    		$(this).find(".zusan").text("组三").addClass("analysis").removeClass("interval");
	    	}else{
	    		$(this).find(".chongfu").text("重复").addClass("analysis").removeClass("interval");
	    }
	    //记录该位置号码的未出现情况，出现归零，下一次从1开始
		if(k==0){
        	$(this).find("td").each(function(){
            	if($(this).html()==""){
             	 	$(this).text("1");
             	}
            });
    
        }else{
        	$(this).find("td").each(function(){
        		if($(this).html()==""){
        			if($(this).parent().next().find("td").eq($(this).index()).is(".analysis")){
                    	$(this).text("1");
                    }else{
                		$(this).text(eval($(this).parent().next().find("td").eq($(this).index()).text()+"+"+1))
                	}
        		}
	        });
            
            //增加绘图
            
	        var node = $(this).find('.td_canvas_100');
	        var node_x = node.offset().left;
			var node_y= node.offset().top + node.height() * 0.5;
			var pre_node = node.parent().next().find('.td_canvas_100');
			var pre_node_x = pre_node.offset().left + pre_node.width() * 0.5;
			var pre_node_y = pre_node.offset().top + pre_node.height() * 0.5;
			var new_node = $("<canvas></canvas>").css({"width":Math.abs(pre_node_x - node_x),"height":Math.abs(pre_node_y - node_y)}).addClass("canvas_100");
			$('body').append(new_node);
			var ctx = new_node.get(0).getContext('2d');
			ctx.beginPath();
			ctx.moveTo(node_x, node_y);
			ctx.lineTo(pre_node_x, pre_node_y);
			ctx.lineWidth = 1.0;
			ctx.strokeStyle = "#000000";
			ctx.stroke(); 

			var node = $(this).find('.td_canvas_10');
	        var node_x = node.offset().left;
			var node_y= node.offset().top + node.height() * 0.5;
			var pre_node = node.parent().next().find('.td_canvas_10');
			var pre_node_x = pre_node.offset().left + pre_node.width() * 0.5;
			var pre_node_y = pre_node.offset().top + pre_node.height() * 0.5;
			var new_node = $("<canvas></canvas>").css({"width":Math.abs(pre_node_x - node_x),"height":Math.abs(pre_node_y - node_y)}).addClass("canvas_10");
			$("body").append(new_node);
			var ctx = new_node.get(0).getContext('2d');
			ctx.beginPath();
			ctx.moveTo(node_x, node_y);
			ctx.lineTo(pre_node_x, pre_node_y);
			ctx.lineWidth = 1.0;
			ctx.strokeStyle = "#000000";
			ctx.stroke(); 


			var node = $(this).find('.td_canvas_1');
	        var node_x = node.offset().left;
			var node_y= node.offset().top + node.height() * 0.5;
			var pre_node = node.parent().next().find('.td_canvas_1');
			var pre_node_x = pre_node.offset().left + pre_node.width() * 0.5;
			var pre_node_y = pre_node.offset().top + pre_node.height() * 0.5;
			var new_node = $("<canvas></canvas>").css({"width":Math.abs(pre_node_x - node_x),"height":Math.abs(pre_node_y - node_y)}).addClass("canvas_1");
			$('body').append(new_node);
			var ctx = new_node.get(0).getContext('2d');
			ctx.beginPath();
			ctx.moveTo(node_x, node_y);
			ctx.lineTo(pre_node_x, pre_node_y);
			ctx.lineWidth = 1.0;
			ctx.strokeStyle = "#000000";
			ctx.stroke(); 

			
			
    	}
	});
});