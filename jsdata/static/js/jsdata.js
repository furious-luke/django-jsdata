'use strict';

(function() {
    var root = this;
    var previous_jsdata = root.jsdata;

    var json_data = JSON.parse( window.jsdata_json || '{}' );

    var jsdata = function( path, default_value ) {
        var links = !path ? [] : path.split( '.' );
        var data = json_data;
        for( var ii = 0; ii < links.length; ++ii ) {
	    if( !data || !data.hasOwnProperty( links[ii] ) )
	        return default_value;
	    data = data[links[ii]];
        }
        return data;
    }

    jsdata.noConflict = function() {
        root.jsdata = previous_jsdata;
        return jsdata;
    }

    if( typeof exports !== 'undefined' ) {
        if( typeof module !== 'undefined' && module.exports ) {
            exports = module.exports = jsdata;
        }
        exports.jsdata = jsdata;
    }
    else
        root.jsdata = jsdata;
    
}).call( this );
