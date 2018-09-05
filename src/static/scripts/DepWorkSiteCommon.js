function getWorkAreaObj()  //获得框架的工作区对象
{
	return window.parent.document.getElementById("workarea")
}

function navigateTo(url)  //菜单导航
{
	getWorkAreaObj().src=url
}