$( document ).ready(function() {

    var uri = null;
    var repo = null;
    var owner = null;
    var current_message = null;
    var socket = io.connect('http://' + document.domain + ':' + 
                            location.port + '/badge');
    socket.on('info', function(msg) {
        current_message = msg;
        put_info('contact', current_message['contact']);
        put_info('doi', current_message['doi'][0]);
        put_info('license', current_message['license'][0]);
    });

    var put_info = function(id, content){
        $('.fa-' + id).removeClass('fa-spin fa-spinner fa-check circle-o-notch');
        if(content){
            $('.fa-' + id).addClass('fa-check');
            $( "input#" + id ).val(content);
        } else {
            $('.fa-' + id).addClass('fa-remove');
        }
    }

    var reload_triggers = function(token) {
        $('.fa-2x').removeClass("circle-o-notch fa-check fa-remove");
        $('.fa-2x').addClass("fa-spinner fa-spin");
        // Here all the websocket thingies will be done!
        socket.emit('get_info', {repo: repo, owner: owner, token: token});
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