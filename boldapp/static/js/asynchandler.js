function GetData(method,url,userdata,successmethod)
{
    $.ajax({
            method: method,
            url: url,
            data:userdata,
            success: successmethod,
            error: function (data) {
                alert("An error occurred!");
                console.log(data);
            }
        });
}

function PostData()
{

}
