(function (window) {
    var byeSpeaker = new Object;
    byeSpeaker.speak = function(name) {
        console.log(speakWord + " " + name);
    }

    var speakWord = "Good Bye";

    window.byeSpeaker = byeSpeaker;
})(window)