
	function y2k(number) { return (number < 1000) ? number + 1900 : number; }

	function dispdate(){
	     var now = new Date();
	     var dd = now.getDate() , mt = now.getMonth() + 1 , yy = y2k(now.getYear()) , weekVal = now.getDay();

	        if (weekVal==0)
	       msg1="sunday";
	    else if (weekVal==1)
	        msg1="monday"; 
	    else if (weekVal==2)
	        msg1="tuesday"; 
	    else if (weekVal==3)
	            msg1="wednesday"; 
	    else if (weekVal==4)
	            msg1="thursday"; 
	    else if (weekVal==5)
	            msg1="friday"; 
	    else if (weekVal==6)
	            msg1="saturday"; 

	   document.write(yy+"-"+mt+"-"+dd+" "+msg1);
	}

	var flasher = false;

	function updateTime() { 
	var now = new Date(); 
	var theHour = now.getHours(); 
	var theMin = now.getMinutes();
	var theSec = now.getSeconds();
	if (theHour<10)
	{
		theHour="0"+theHour
	}
	if(theMin<10)
	{
		theMin="0"+theMin
	}
	if(theSec<10)
	{
		theSec="0"+theSec
	}
	var theTime = theHour + ":"+theMin+":"+theSec;
	flasher = !flasher;
	lblTime.innerHTML = theTime; 
	// recursively call this function every second to keep timer going 
	timerID = setTimeout("updateTime()",1000);
	} 	