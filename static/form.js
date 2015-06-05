$( document ).ready(function() {

    var uri = null;
    var repo = null;
    var owner = null;
    var socket = io.connect('http://' + document.domain + ':' + 
                            location.port + '/badge');
    socket.on('info', function(msg) {
        console.log(msg);
    });

    var reload_triggers = function(token) {
        $('.fa-2x').removeClass("circle-o-notch fa-check fa-remove");
        $('.fa-2x').addClass("fa-spinner fa-spin");
        // Here all the websocket thingies will be done!
        socket.emit('get info', {repo: repo, owner: owner, token: token});
    };

    var split_uri = function() {
        uri = window.location.href;
        var parser = document.createElement('a');
        parser.href = uri;
        var repo_and_owner = parser.pathname.split('/');
        owner = repo_and_owner[1];
        repo = repo_and_owner[2];
    }


    $('[data-toggle="tooltip"]').tooltip();

    $('.btn-success').click(function() {
        reload_triggers($( "input#zenodo_token" ).val());
    });

    $('.submit').click(function() {
        reload_triggers($( "input#zenodo_token" ).val());
    });

    split_uri();

});