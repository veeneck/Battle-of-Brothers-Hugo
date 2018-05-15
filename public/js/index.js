$(document).ready(function () {

        var disqusPublicKey = "msqb9E8qDaEGRmXysyMYipQqutxljqNDo4zQmNsql13tmdH1TxqvuGDAvTmYZPG0";
        var disqusShortname = "battle-of-brothers";
        var urlArray = [];

        $('.my-class').each(function () {
            console.log("looking for comment count");
            var url = $(this).attr('data-disqus-url');
            urlArray.push('link:' + url);
        });


        $('#some-button').click(function () {
            $.ajax({
               type: 'GET',
               url: "https://disqus.com/api/3.0/threads/set.jsonp",
               data: { api_key: disqusPublicKey, forum : disqusShortname, thread : urlArray }, // URL method
               cache: false,
               dataType: 'jsonp',
               success: function (result) {

                    for (var i in result.response) {

                        var countText = " comments";
                        var count = result.response[i].posts;

                        if (count == 1)
                           countText = " comment";

                        $('span[data-disqus-url="' + result.response[i].link + '"]').html('' + count + countText);

                    }
                }
        });
      });

});