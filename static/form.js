$( document ).ready(function() {

    var uri = null;
    var repo = null;
    var owner = null;

    var reload_triggers = function() {
        // Here all the Ajax requests will be done!
    };

    var split_uri = function() {
        uri = window.location.href;
        var parser = document.createElement('a');
        parser.href = uri;
        var repo_and_owner = parser.pathname.split('/');
        owner = repo_and_owner[1];
        repo = repo_and_owner[2];
    }

    $('[data-toggle="tooltip"]').tooltip()

    $('.btn-success').click(function() {
        reload_triggers();
    })

    // When the page is started, read the data as well.
    split_uri();
    reload_triggers();
});