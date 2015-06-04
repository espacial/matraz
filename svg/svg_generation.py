def main():
	image = matraz_svg('MIT', True, True, '10.1234/hola')
	f = open('matraz.svg', 'w')
	f.write(image)
	f.close()

def matraz_svg (license=None, contact=False, documentation=False, doi=None, size='150mm'):
	header= """<?xml version="1.0" encoding="UTF-8" standalone="no"?>

<svg
	xmlns:dc="http://purl.org/dc/elements/1.1/"
	xmlns:cc="http://creativecommons.org/ns#"
	xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	xmlns:svg="http://www.w3.org/2000/svg"
	xmlns="http://www.w3.org/2000/svg"
	xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
	xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
	sodipodi:docname="matraz_colores.svg"
	inkscape:version="0.91 r13725"
	version="1.1"
	id="svg4179"
	viewBox="0 0 744.09448819 1052.3622047"
	height="150mm"
	width="100mm">
	<sodipodi:namedview
		inkscape:window-maximized="0"
		inkscape:window-y="0"
		inkscape:window-x="51"
		inkscape:window-height="755"
		inkscape:window-width="1225"
		showgrid="false"
		inkscape:current-layer="layer1"
		inkscape:document-units="px"
		inkscape:cy="787.36824"
		inkscape:cx="333.10863"
		inkscape:zoom="8.0000002"
		inkscape:pageshadow="2"
		inkscape:pageopacity="0.0"
		borderopacity="1.0"
		bordercolor="#666666"
		pagecolor="#ffffff"
		id="base" />
	<script
	type="text/javascript"
	id="inkwebjs"><![CDATA[
	var InkWeb = {
		version: 0.04,
		NS: {
			svg:	  "http://www.w3.org/2000/svg",
			sodipodi: "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd",
			inkscape: "http://www.inkscape.org/namespaces/inkscape",
			cc:	   "http://creativecommons.org/ns#",
			dc:	   "http://purl.org/dc/elements/1.1/",
			rdf:	  "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
			xlink:	"http://www.w3.org/1999/xlink",
			xml:	  "http://www.w3.org/XML/1998/namespace"
		}

	};

	InkWeb.el = function (tag, attributes) {
		// A helper to create SVG elements
		var element = document.createElementNS( this.NS.svg, tag );
		for ( var att in attributes ) {
			switch ( att ) {
				case "parent":
					attributes.parent.appendChild( element );
					break;
				case "text":
					element.appendChild( document.createTextNode( attributes.text ) );
					break;
				default:
					element.setAttribute( att, attributes[att] );
			}
		}
		return element;
	}

	InkWeb.reGetStyleAttVal = function (att) {
		return new RegExp( "(^|.*;)[ ]*"+ att +":([^;]*)(;.*|$)" )
	}

	InkWeb.getStyle = function (el, att) {
		// This method is needed because el.style is only working
		// to HTML style in the Firefox 3.0
		if ( typeof(el) == "string" )
			el = document.getElementById(el);
		var style = el.getAttribute("style");
		var match = this.reGetStyleAttVal(att).exec(style);
		if ( match ) {
			return match[2];
		} else {
			return false;
		}
	}

	InkWeb.setStyle = function (el, att, val) {
		if ( typeof(el) == "string" )
			el = document.getElementById(el);
			var style = el.getAttribute("style");
			re = this.reGetStyleAttVal(att);
		if ( re.test(style) ) {
			style = style.replace( re, "$1"+ att +":"+ val +"$3" );
		} else {
			style += ";"+ att +":"+ val;
		}
		el.setAttribute( "style", style );
		return val
	}

	InkWeb.transmitAtt = function (conf) {
		conf.att = conf.att.split( /\s+/ );
		if ( typeof(conf.from) == "string" )
			conf.from = document.getElementById( conf.from );
		if ( ! conf.to.join )
			conf.to = [ conf.to ];
		for ( var toEl,elN=0; toEl=conf.to[elN]; elN++ ) {
			if ( typeof(toEl) == "string" )
				toEl = document.getElementById( toEl );
			for ( var i=0; i<conf.att.length; i++ ) {
				var val = this.getStyle( conf.from, conf.att[i] );
				if ( val ) {
					this.setStyle( toEl, conf.att[i], val );
				} else {
					val = conf.from.getAttribute(conf.att[i]);
					toEl.setAttribute( conf.att[i], val );
					}
			}
		}
	}

	InkWeb.setAtt = function (conf) {
		if ( ! conf.el.join )
			conf.to = [ conf.el ];
		conf.att = conf.att.split( /\s+/ );
		conf.val = conf.val.split( /\s+/ );
		for ( var el,elN=0; el=conf.el[elN]; elN++ ) {
			if ( typeof(el) == "string" )
				el = document.getElementById( el );
			for ( var att,i=0; att=conf.att[i]; i++ ) {
				if (
					att == "width"  ||
					att == "height" ||
					att == "x"  ||
					att == "y"  ||
					att == "cx" ||
					att == "cy" ||
					att == "r"  ||
					att == "rx" ||
					att == "ry" ||
					att == "transform"
				) {
					el.setAttribute( att, conf.val[i] );
				} else {
					this.setStyle( el, att, conf.val[i] );
				}
			}
		}
	}

	InkWeb.moveElTo = function (startConf) {
		if ( typeof(startConf) == "string" ) {
			// startConf may be only a element Id, to timeout recursive calls.
			var el = document.getElementById( startConf );
		} else {
			if ( typeof(startConf.el) == "string" )
				startConf.el = document.getElementById( startConf.el );
			var el = startConf.el;
		}
		if ( ! el.inkWebMoving ) {
			el.inkWebMoving = {
				step: 0
				};
		}
		var conf = el.inkWebMoving;
		if ( conf.step == 0 ) {
			conf.x = startConf.x;
			conf.y = startConf.y;
			// dur : duration of the animation in seconds
			if ( startConf.dur ) { conf.dur = startConf.dur }
			else { conf.dur = 1 }
			// steps : animation steps in a second
			if ( startConf.stepsBySec ) { conf.stepsBySec = startConf.stepsBySec }
			else { conf.stepsBySec = 16 }
			conf.sleep = Math.round( 1000 / conf.stepsBySec );
			conf.steps = conf.dur * conf.stepsBySec;
			var startPos = el.getBBox();
			conf.xInc = ( conf.x - startPos.x ) / conf.steps;
			conf.yInc = ( conf.y - startPos.y ) / conf.steps;
			conf.transform = el.transform.baseVal.consolidate();
			if ( ! conf.transform ) {
				conf.transform = el.ownerSVGElement.createSVGTransform();
			}
			el.transform.baseVal.clear();
			el.transform.baseVal.appendItem(conf.transform);
		}
		if ( conf.step < conf.steps ) {
			conf.step++;
			conf.transform.matrix.e += conf.xInc;
			conf.transform.matrix.f += conf.yInc;
			try{ el.ownerSVGElement.forceRedraw() }
			catch(e){ this.log(e, "this "+el.ownerSVGElement+" has no forceRedraw().") }
			conf.timeout = setTimeout( 'InkWeb.moveElTo("'+el.id+'")', conf.sleep );
		} else {
			delete el.inkWebMoving;
		}
	}

	InkWeb.log = function () { /* if you need that, use the inkweb-debug.js too */ }
	]]></script>
	<defs id="defs4181" />
	<metadata id="metadata4184">
		<rdf:RDF>
		<cc:Work rdf:about="">
		<dc:format>image/svg+xml</dc:format>
		<dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
		</cc:Work>
		</rdf:RDF>
	</metadata>

	<g id="layer1" inkscape:groupmode="layer" inkscape:label="Layer 1">
	"""

	border = """
	<g
		style="fill:#cccccc;stroke:none;stroke-opacity:1;stroke-width:5.16;
			stroke-miterlimit:4;stroke-dasharray:none"
		transform="matrix(1.25,0,0,-1.25,96.861045,319.86484)"
		id="g3785">
	<path
		inkscape:connector-curvature="0"
		id="path3787"
		style="fill:#cccccc;fill-opacity:1;fill-rule:nonzero;stroke:none;    
			stroke-opacity:1;stroke-width:5.16;stroke-miterlimit:4;
			stroke-dasharray:none"
		d="m 0,0 c -30.55,0 -55.31,24.767 -55.31,55.329 0,25.086 16.714,46.266 39.612,53.032 l 0,7.712 16.32,0 c 1.064,0 1.916,0.854 1.916,1.905 0,1.053 -0.852,1.905 -1.916,1.905 l -16.32,0 0,7.63 16.32,0 c 1.064,0 1.916,0.85 1.916,1.905 0,1.048 -0.852,1.898 -1.916,1.898 l -16.32,0 0,7.622 16.32,0 c 1.064,0 1.916,0.857 1.916,1.908 0,1.049 -0.852,1.905 -1.916,1.905 l -16.32,0 0,7.246 c -4.423,0.635 -7.825,4.399 -7.825,8.995 0,5.05 4.087,9.139 9.134,9.139 l 28.776,0 c 5.059,0 9.136,-4.089 9.136,-9.139 0,-4.596 -3.405,-8.36 -7.826,-8.995 l 0,-41.636 C 38.601,101.593 55.313,80.412     55.313,55.328 55.313,24.767 30.542,0 0,0 m 24.134,114.325 0,30.108 c 4.74,3.179 7.824,8.586 7.824,14.563 0,9.692 -7.884,17.577 -17.575,17.577 l -28.772,0 c -9.69,0 -17.569,-7.885 -17.569,-17.577 0,-5.976 3.087,-11.381 7.823,-14.563 l 0,-30.108 c -23.61,-9.692 -39.614,-33.101 -39.614,-58.996 0,-35.163 28.598,-63.764 63.749,-63.764 35.151,0 63.752,28.601 63.752,63.764 0,25.895 -16.003,49.305 -39.618,58.996" />
	</g>
 	"""

	background = """
	<ellipse
		style="fill:#ffffff;fill-opacity:1;stroke:none;stroke-width:1;
			stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
		id="path9840"
		cx="125.5"
		cy="252.6122"
		rx="44"
		ry="65.25" />
	"""

	color_first = """
    
	<ellipse
		onmouseover="   ; InkWeb.setStyle(this, 'fill', '#d2ed1a')
				; InkWeb.setStyle('rect9652', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5075', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5077', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5079', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path9898', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5083', 'fill', '#d2ed1a')"
		onmouseout="    ; InkWeb.setStyle(this, 'fill', '#d2ed1a')
				; InkWeb.setStyle('rect9652', 'fill', '#b3b3b3')
				; InkWeb.setStyle('path5075', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5077', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path9898', 'fill', '#b3b3b3')
				; InkWeb.setStyle('path5079', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5083', 'fill', '#d2ed1a')"
		ry="10.921379"
		rx="10.626206"
		cy="30.150023"
		cx="130.10428"
		id="path5081"
		style="fill:#d2ed1a;fill-opacity:1;stroke:none;stroke-width:2;
		stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
    
	<ellipse
		onmouseover="   ; InkWeb.setStyle(this, 'fill', '#d2ed1a')
				; InkWeb.setStyle('rect9652', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5075', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5077', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path9898', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5083', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5081', 'fill', '#d2ed1a')"
		onmouseout="    ; InkWeb.setStyle(this, 'fill', '#d2ed1a')
				; InkWeb.setStyle('rect9652', 'fill', '#b3b3b3')
				; InkWeb.setStyle('path5075', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5077', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path9898', 'fill', '#b3b3b3')
				; InkWeb.setStyle('path5083', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5081', 'fill', '#d2ed1a')"
		ry="5.3131032"
		rx="4.7227588"
		cy="52.878311"
		cx="120.06842"
		id="path5079"
		style="fill:#d2ed1a;fill-opacity:1;stroke:none;stroke-width:2;
		stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
    
	<ellipse
		onmouseover="   ; InkWeb.setStyle(this, 'fill', '#d2ed1a')
				; InkWeb.setStyle('rect9652', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5075', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5083', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path9898', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5079', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5081', 'fill', '#d2ed1a')"
		onmouseout="    ; InkWeb.setStyle(this, 'fill', '#d2ed1a')
				; InkWeb.setStyle('rect9652', 'fill', '#b3b3b3')
				; InkWeb.setStyle('path5075', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5083', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path9898', 'fill', '#b3b3b3')
				; InkWeb.setStyle('path5079', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5081', 'fill', '#d2ed1a')"
		ry="5.9034481"
		rx="6.1986208"
		cy="64.685196"
		cx="104.42429"
		id="path5077"
		style="fill:#d2ed1a;fill-opacity:1;stroke:none;stroke-width:2;
		stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
    
	<path
		onmouseover="   ; InkWeb.setStyle(this, 'fill', '#d2ed1a')
				; InkWeb.setStyle('rect9652', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5075', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5077', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5079', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path9898', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5081', 'fill', '#d2ed1a')"
		onmouseout="    ; InkWeb.setStyle(this, 'fill', '#d2ed1a')
				; InkWeb.setStyle('rect9652', 'fill', '#b3b3b3')
				; InkWeb.setStyle('path5075', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5077', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path9898', 'fill', '#b3b3b3')
				; InkWeb.setStyle('path5079', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5081', 'fill', '#d2ed1a')"
		style="fill:#d2ed1a;fill-opacity:1;fill-rule:evenodd;stroke:none;
			stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;
			stroke-opacity:1"
		d="m 78.989685,97.617157 c 16.66229,-0.31559 13.88684,0.75513 36.010995,-0.22359 0,0 6.35845,0.149 12.69626,4.171323 9.15712,5.81162 17.81714,18.34708 3.38629,38.78062 -3.34927,4.74244 -4.21347,13.75723 0.29517,17.41517 4.43553,3.59863 11.75379,3.10812 14.32021,-1.99459 2.55076,-5.07157 -5.34169,-9.74138 -4.45725,-15.34896 0.88908,-5.63699 8.27781,-6.72296 8.88484,-12.39725 0.72337,-6.76178 -5.86944,-10.64353 -6.4938,-17.41517 -0.60901,-6.60516 6.88434,-13.254183 2.95173,-18.595863 -3.74059,-5.08087 -13.41379,1.06541 -18.89104,-2.06621 -6.41752,-3.66922 -2.74607,-15.30211 -10.03586,-16.52965 -7.6852,-1.29412 -9.03212,7.27527 -16.82482,7.37931 -10.932815,0.14597 -13.331035,-8.52956 -24.204145,-7.37931 -10.45292,1.1058 -20.6678,9.5353 -18.30069,19.77655 0.88241,3.81772 6.41546,5.7564 10.33103,5.60828 3.62721,-0.13722 10.33104,-1.18069 10.33104,-1.18069 z"
		id="path5083"
		inkscape:connector-curvature="0"
		sodipodi:nodetypes="ccsssssssssssssscc" />
    
	<path
		onmouseover="   ; InkWeb.setStyle(this, 'fill', '#d2ed1a')
				; InkWeb.setStyle('rect9652', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5083', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5077', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path9898', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5079', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5081', 'fill', '#d2ed1a')"
		onmouseout="    ; InkWeb.setStyle(this, 'fill', '#d2ed1a')
				; InkWeb.setStyle('rect9652', 'fill', '#b3b3b3')
				; InkWeb.setStyle('path5083', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5077', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path9898', 'fill', '#b3b3b3')
				; InkWeb.setStyle('path5079', 'fill', '#d2ed1a')
				; InkWeb.setStyle('path5081', 'fill', '#d2ed1a')"
		sodipodi:nodetypes="ccccccsssscscccssscscc"
		inkscape:connector-curvature="0"
		id="path5075"
		d="m 73.238435,113.52274 c -2.11275,1.54321 -3.05604,6.35969 -3.05604,6.35969 0,0 -0.59692,5.37448 1.58255,7.26688 1.52316,2.94664 5.00367,2.36661 6.98861,3.69072 1.76848,1.33067 1.26329,3.50456 1.26329,3.50456 l -0.23949,53.72264 c 0,0    -6.63346,6.28146 -5.61263,8.26484 3.79005,7.36367 16.98809,-6.65772 25.21627,-7.59852 1.368565,-0.15648 1.710685,0.74904 2.681875,1.10472 3.66079,1.34068 4.67417,7.65481 8.56,7.96966 1.76797,0.14325 4.72276,-2.36139 4.72276,-2.36139 0,0 6.26667,2.39071 6.85081,0.28252 0.73262,-2.64405 -8.47426,-7.80938 -8.47426,-7.80938 l -0.0593,-54.45833 0.30553,-2.65591 c 0,0 5.22218,-1.60249 6.92568,-3.15715 1.99404,-1.81981 3.05321,-3.49228 3.15915,-6.18981 0.11665,-2.9702 -0.70904,-5.22328 -2.80414,-7.3319 -1.71067,-1.72172 -6.19862,-2.65655 -6.19862,-2.65655 -18.710365,0.45724 -30.258185,-0.17777 -36.758235,0.32159 -3.14094,0.24129 -5.05379,1.73112 -5.05379,1.73112 z"
		style="fill:#d2ed1a;fill-opacity:1;fill-rule:evenodd;stroke:none;    
			stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;
			stroke-opacity:1" />	
	"""	

	color_second = """
    
	<path
		onmouseover="   ; InkWeb.setStyle(this, 'fill', '#99cc00')
				; InkWeb.setStyle('path9898-6', 'fill', '#99cc00')
				; InkWeb.setStyle('rect9652-6', 'fill', '#99cc00')"
		onmouseout="    ; InkWeb.setStyle(this, 'fill', '#99cc00')
				; InkWeb.setStyle('path9898-6', 'fill', '#b3b3b3')
				; InkWeb.setStyle('rect9652-6', 'fill', '#b3b3b3')"
		sodipodi:nodetypes="csssccssssssssssssccssscssssssssssscssssssssscccssccc"
		inkscape:connector-curvature="0"
		id="path5059"
		d="m 125.00634,191.19889 c -1.43008,0.25502 -4.55438,-0.18273 -5.89349,0.24569 -0.96095,0.3074 -1.86696,0.66453 -2.6735,1.08098 -0.80653,0.41646 -1.51364,0.89169 -2.0759,1.4337 -0.61332,0.59126 -1.22017,0.89276 -1.82397,0.96895 -0.60379,0.0761 -1.2032,-0.0722 -1.80523,-0.38383 -1.20406,-0.62315 -2.41273,-1.89471 -3.65627,-3.30521 -1.24354,-1.4105 -2.52357,-2.95971 -3.86866,-4.13929 -0.67253,-0.58978 -1.36009,-1.08842 -2.06965,-1.42955 -0.70957,-0.34114 -1.440255,-0.52655 -2.194605,-0.49174 -0.97352,0.0449 -1.88613,0.20772 -2.75469,0.45646 -0.86855,0.24874 -1.6926,0.58381 -2.48609,0.97931 -1.58699,0.79103 -3.05411,1.81912 -4.52036,2.85498 -1.46625,1.03587 -2.93134,2.08037 -4.5162,2.90477 -0.79242,0.41218 -1.61498,0.76986 -2.48194,1.04363 -0.86695,0.27376 -1.77912,0.46323 -2.75053,0.54152 -1.14647,0.0924 -2.50696,-0.21437 -3.90195,-0.72618 -1.39499,-0.51181 -2.82343,-1.22794 -4.11018,-1.95657 -0.6008,-0.34021 -0.99301,0.0781 -1.51316,-0.24746 -13.27714,5.80995 -23.78868,15.36879 -30.71029,27.99831 1.38258,1.38307 3.04191,3.00067 5.09503,4.71401 2.33113,1.94534 4.97491,3.8885 7.66443,5.34062 1.34475,0.72606 2.70175,1.32955 4.0352,1.74909 1.33347,0.41952 2.64499,0.65651 3.89989,0.64733 1.01813,-0.007 1.9493,-0.21051 2.81715,-0.5602 0.86787,-0.34969 1.67145,-0.84698 2.43197,-1.442 1.52104,-1.19004 2.87146,-2.77352 4.22053,-4.36336 1.34908,-1.58986 2.69808,-3.18645 4.21844,-4.40072 0.76019,-0.60714 1.56252,-1.11771 2.42989,-1.48559 0.86736,-0.36786 1.7997,-0.59284 2.81714,-0.62452 1.25546,-0.0391 2.42603,0.1603 3.53343,0.53738 1.10741,0.37708 2.15071,0.93314 3.15239,1.60799 2.00335,1.34973 3.83743,3.17603 5.67179,5.00656 1.83436,1.83055 3.66998,3.6651 5.67388,5.0294 1.00195,0.68214 2.04457,1.24694 3.152385,1.63497 1.10781,0.38802 2.27953,0.59921 3.5355,0.57473 1.0233,-0.0199 1.96663,-0.22983 2.85047,-0.58096 0.88384,-0.35113 1.70811,-0.84441 2.49235,-1.43164 1.56848,-1.17443 2.97791,-2.72573 4.38711,-4.27414 1.40919,-1.54842 2.81837,-3.09364 4.38709,-4.25548 0.78438,-0.58092 1.60832,-1.06506 2.49234,-1.40673 0.88403,-0.34167 1.82901,-0.5404 2.85256,-0.54776 1.17408,-0.008 2.26132,0.21021 3.28357,0.59756 1.02224,0.38734 1.97836,0.94334 2.89211,1.61214 1.82749,1.33761 3.48103,3.12334 5.1346,4.90074 1.65356,1.77741 3.30822,3.54638 5.13458,4.84889 0.91321,0.65125 1.86865,1.18679 2.89004,1.54781 1.02141,0.36102 2.10852,0.54773 3.28149,0.50419 0.9093,-0.0338 1.88639,-0.24982 2.89627,-0.59963 1.0099,-0.34981 2.05241,-0.83446 3.08993,-1.40881 2.07503,-1.14871 4.13215,-2.65388 5.88001,-4.15173 0.37737,-0.32341 0.52267,-0.56702 0.86825,-0.88596 -6.1461,-16.492 -17.11351,-29.14994 -33.35515,-36.26265 z"
		style="fill:#99cc00;fill-opacity:1;stroke:#ffffff;
			stroke-width:2.12837362;stroke-miterlimit:4;
			stroke-dasharray:none;stroke-opacity:1" />
    
	<ellipse
		ry="5.2531981"
		rx="5.0492411"
		cy="196.28099"
		cx="98.946747"
		id="path5069"
		style="fill:#ffffff;stroke:#ffffff;stroke-width:1.64502656;
		stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
	"""

	color_third = """
    
	<path
		onmouseover="   ; InkWeb.setStyle(this, 'fill', '#669900')
				; InkWeb.setStyle('path9898-5', 'fill', '#669900')
				; InkWeb.setStyle('rect9652-0', 'fill', '#669900')"
		onmouseout="    ; InkWeb.setStyle(this, 'fill', '#669900')
				; InkWeb.setStyle('path9898-5', 'fill', '#b3b3b3')
				; InkWeb.setStyle('rect9652-0', 'fill', '#b3b3b3')"
		inkscape:connector-curvature="0"
		id="path5051"
		d="m 158.36149,227.46154 c -0.34558,0.31894 -0.49088,0.56255    -0.86825,0.88596 -1.74786,1.49785 -3.80498,3.00302 -5.88001,4.15173    -1.03752,0.57435 -2.08003,1.059 -3.08993,1.40881 -1.00988,0.34981    -1.98697,0.56587 -2.89627,0.59963 -1.17297,0.0436 -2.26008,-0.14317    -3.28149,-0.50419 -1.02139,-0.36102 -1.97685,-0.89656 -2.89004,-1.54781    -1.82637,-1.30251 -3.48102,-3.07148 -5.13458,-4.84889 -1.65357,-1.7774    -3.30711,-3.56313 -5.1346,-4.90074 -0.91375,-0.6688 -1.86987,-1.2248    -2.89211,-1.61214 -1.02225,-0.38735 -2.10949,-0.60601 -3.28357,-0.59756    -1.02355,0.007 -1.96853,0.20609 -2.85256,0.54776 -0.88402,0.34167    -1.70796,0.82581 -2.49234,1.40673 -1.56872,1.16184 -2.9779,2.70706    -4.38709,4.25548 -1.4092,1.54841 -2.81863,3.09971 -4.38711,4.27414    -0.78424,0.58723 -1.60851,1.08051 -2.49235,1.43164 -0.88384,0.35113    -1.82717,0.56098 -2.85047,0.58096 -1.25597,0.0245 -2.42769,-0.18671    -3.5355,-0.57473 -1.107815,-0.38803 -2.150435,-0.95283    -3.152385,-1.63497 -2.0039,-1.3643 -3.83952,-3.19885 -5.67388,-5.0294    -1.83436,-1.83053 -3.66844,-3.65683 -5.67179,-5.00656 -1.00168,-0.67485    -2.04498,-1.23091 -3.15239,-1.60799 -1.1074,-0.37708 -2.27797,-0.57646    -3.53343,-0.53738 -1.01744,0.0317 -1.94978,0.25666 -2.81714,0.62452    -0.86737,0.36788 -1.6697,0.87845 -2.42989,1.48559 -1.52036,1.21427    -2.86936,2.81086 -4.21844,4.40072 -1.34907,1.58984 -2.69949,3.17332    -4.22053,4.36336 -0.76052,0.59502 -1.5641,1.09231 -2.43197,1.442    -0.86785,0.34969 -1.79902,0.55277 -2.81715,0.5602 -1.2549,0.009    -2.56642,-0.22781 -3.89989,-0.64733 -1.33345,-0.41954 -2.69045,-1.02303    -4.0352,-1.74909 -2.68952,-1.45212 -5.3333,-3.39528 -7.66443,-5.34062    -2.05312,-1.71334 -3.71245,-3.33094 -5.09503,-4.71401 a    65.639627,64.965206 0 0 0 -7.97675,30.91082 65.639627,64.965206 0 0 0    9.5925,33.69731 c 0.95485,-1.0689 1.69143,-1.99747 2.83381,-3.13715    1.13801,-1.1353 2.35214,-2.2695 3.61047,-3.33217 1.25832,-1.06267    2.55983,-2.05523 3.87281,-2.90269 1.31297,-0.84745 2.6375,-1.54989    3.93944,-2.03955 1.30194,-0.48967 2.58094,-0.76593 3.80618,-0.75525    0.99405,0.008 1.90526,0.24542 2.7526,0.65358 0.84736,0.40816    1.63113,0.98817 2.37366,1.68268 1.48509,1.38903 2.80341,3.23805    4.1206,5.09371 1.31717,1.85566 2.63408,3.7179 4.1185,5.1352    0.74221,0.70865 1.52472,1.30518 2.37157,1.73456 0.84687,0.42937    1.75714,0.6913 2.75053,0.72827 1.22578,0.0457 2.36891,-0.18648    3.45015,-0.6266 1.08122,-0.44012 2.1015,-1.08796 3.07951,-1.87564    1.95599,-1.57538 3.74545,-3.7082 5.53645,-5.8448 1.79099,-2.1366    3.58201,-4.27728 5.53853,-5.86969 0.97825,-0.7962 1.9979,-1.45596    3.07951,-1.90885 1.08161,-0.45289 2.225935,-0.69876 3.452225,-0.67017    0.9991,0.0233 1.92089,0.26864 2.78384,0.67847 0.86294,0.40983    1.66625,0.98485 2.43196,1.67024 1.5314,1.3708 2.90712,3.1806    4.28299,4.98788 1.37588,1.80731 2.75344,3.61106 4.28508,4.96715    0.76582,0.67805 1.56883,1.24446 2.43196,1.64327 0.86312,0.3988    1.78451,0.63045 2.78384,0.63904 1.14633,0.0104 2.20844,-0.24502    3.20653,-0.69714 0.99807,-0.45211 1.93334,-1.10124 2.82548,-1.88186    1.78429,-1.56125 3.39936,-3.64573 5.01384,-5.72032 1.61447,-2.07458    3.22855,-4.13985 5.01174,-5.66013 0.8916,-0.76015 1.82407,-1.38371    2.82133,-1.8051 0.99726,-0.42139 2.0592,-0.64007 3.20443,-0.58926    0.88781,0.0394 1.84156,0.28886 2.82758,0.69715 0.98601,0.40829    2.00405,0.97496 3.01703,1.64534 2.02599,1.34077 4.03399,3.09851    5.74051,4.84681 0.87339,0.89475 1.33448,1.61804 2.01137,2.45037 a    65.639627,64.965206 0 0 0 6.32143,-27.63466 65.639627,64.965206 0 0 0    -4.14142,-22.47664 z"
		style="fill:#669900;fill-opacity:1;stroke:#ffffff;
			stroke-width:2.12837362;stroke-miterlimit:4;
			stroke-dasharray:none; stroke-opacity:1" />
    
	<ellipse
		ry="3.8982375"
		rx="3.9120033"
		cy="263.90689"
		cx="117.19235"
		id="path5065"
		style="fill:#ffffff;stroke:#ffffff;stroke-width:1.2501123;
		stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
    
	<ellipse
		ry="6.6517272"
		rx="6.6752167"
		cy="240.40416"
		cx="82.481201"
		id="path5067"
		style="fill:#ffffff;stroke:#ffffff;stroke-width:1.06418681;
		stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
    
	<ellipse
		ry="4.4952116"
		rx="4.2885776"
		cy="230.20482"
		cx="124.53506"
		id="path5071"
		style="fill:#ffffff;stroke:#ffffff;stroke-width:1.83098149;
		stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
	"""
	
	color_fourth = """
    
	<path
		onmouseover="   ; InkWeb.setStyle(this, 'fill', '#61190f')
				; InkWeb.setStyle('path9898-9', 'fill', '#61190f')
				; InkWeb.setStyle('rect9652-2', 'fill', '#61190f')"
		onmouseout="    ; InkWeb.setStyle(this, 'fill', '#61190f')
				; InkWeb.setStyle('path9898-9', 'fill', '#b3b3b3')
				; InkWeb.setStyle('rect9652-2', 'fill', '#b3b3b3')"
		inkscape:connector-curvature="0"
		id="path5048"
		d="m 156.18148,277.57284 c -0.67689,-0.83233 -1.13798,-1.55562 -2.01137,-2.45037 -1.70652,-1.7483 -3.71452,-3.50604 -5.74051,-4.84681 -1.01298,-0.67038 -2.03102,-1.23705 -3.01703,-1.64534 -0.98602,-0.40829 -1.93977,-0.65774 -2.82758,-0.69715 -1.14523,-0.0508 -2.20717,0.16787 -3.20443,0.58926 -0.99726,0.42139 -1.92973,1.04495 -2.82133,1.8051 -1.78319,1.52028 -3.39727,3.58555 -5.01174,5.66013 -1.61448,2.07459 -3.22955,4.15907 -5.01384,5.72032 -0.89214,0.78062 -1.82741,1.42975 -2.82548,1.88186 -0.99809,0.45212 -2.0602,0.70701 -3.20653,0.69714 -0.99933,-0.008 -1.92072,-0.24024 -2.78384,-0.63904 -0.86313,-0.39881 -1.66614,-0.96522 -2.43196,-1.64327 -1.53164,-1.35609 -2.9092,-3.15984 -4.28508,-4.96715 -1.37587,-1.80728 -2.75159,-3.61708 -4.28299,-4.98788 -0.76571,-0.68539 -1.56902,-1.26041 -2.43196,-1.67024 -0.86295,-0.40983 -1.78474,-0.65517 -2.78384,-0.67847 -1.22629,-0.0286 -2.370615,0.21728 -3.452225,0.67017-1.08161,0.45289 -2.10126,1.11265 -3.07951,1.90885 -1.95652,1.59241 -3.74754,3.73309 -5.53853,5.86969 -1.791,2.1366 -3.58046,4.26942 -5.53645,5.8448 -0.97801,0.78768 -1.99829,1.43552 -3.07951,1.87564 -1.08124,0.44012 -2.22437,0.67221 -3.45015,0.6266 -0.99339,-0.0369 -1.90366,-0.2989 -2.75053,-0.72827 -0.84685,-0.42938 -1.62936,-1.02591 -2.37157,-1.73456 -1.48442,-1.4173 -2.80133,-3.27954 -4.1185,-5.1352 -1.31719,-1.85566 -2.63551,-3.70468 -4.1206,-5.09371 -0.74253,-0.69451 -1.5263,-1.27452 -2.37366,-1.68268 -0.84734,-0.40816 -1.75855,-0.64488 -2.7526,-0.65358 -1.22524,-0.0107 -2.50424,0.26558 -3.80618,0.75525 -1.30194,0.48966 -2.62647,1.1921 -3.93944,2.03955 -1.31298,0.84746 -2.61449,1.84002 -3.87281,2.90269 -1.25833,1.06267 -2.47246,2.19687 -3.61047,3.33217 -1.14238,1.13967 -1.87896,2.06825 -2.83381,3.13715 a 65.639627,64.965206 0 0 0 56.04749,31.26768 65.639627,64.965206 0 0 0 59.318565,-37.33033 z"
		style="fill:#61190f;fill-opacity:1" />
    
	<ellipse
		ry="6.7298188"
		rx="6.531076"
		cy="299.16104"
		cx="110.51712"
		id="path5061"
		style="fill:#ffffff;stroke:#ffffff;stroke-width:1.35195971;
		stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
    
	<ellipse
		ry="2.4663646"
		rx="2.5773823"
		cy="282.72061"
		cx="137.43152"
		id="path5063"
		style="fill:#ffffff;stroke:#ffffff;stroke-width:0.89540923;
		stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1" />
	"""

	box_first = """
	<rect
		style="fill:#b3b3b3;fill-opacity:1;stroke:none;stroke-width:2;
			stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
		id="rect9652"
		width="346.56564"
		height="35.74062"
		x="118.85989"
		y="-183.94012"
		transform="scale(1,-1)"
		ry="5.9727135" />
    
	<rect
		style="fill:#ffffff"
		id="rect3372"
		width="340.75"
		height="30"
		x="121.49999"
		y="-181.11221"
		ry="3.8691864"
		transform="scale(1,-1)" />
    
	<path
		inkscape:connector-curvature="0"
		style="fill:#b3b3b3;fill-opacity:1"
		d="m 200.01934,177.65509 c -1.242,0 -2.43897,-0.15 -3.591,-0.45 -1.15203,-0.30007 -2.2275,-0.72081 -3.2265,-1.2625 -0.999,-0.54169 -1.90803,-1.19169 -2.727,-1.95 -0.81897,-0.75824 -1.52097,-1.6 -2.106,-2.525 -0.58503,-0.92507 -1.0395,-1.92081 -1.3635,-2.9875 -0.324,-1.06669 -0.486,-2.175 -0.486,-3.325 0,-1.15 0.162,-2.25831 0.486,-3.325 0.324,-1.06669 0.77847,-2.0625 1.3635,-2.9875 0.58503,-0.925 1.28703,-1.76669 2.106,-2.525 0.81897,-0.7583 1.728,-1.4083 2.727,-1.94999 0.999,-0.5417 2.07447,-0.9625 3.2265,-1.2625 1.15203,-0.3 2.349,-0.45 3.591,-0.45 1.85403,0 3.6045,0.32919 5.2515,0.9875 1.647,0.6583 3.078,1.55 4.293,2.67499 1.215,1.125 2.17803,2.45 2.889,3.975 0.71097,1.525 1.0665,3.14581 1.0665,4.8625 0,1.15 -0.162,2.25831 -0.486,3.325 -0.32408,1.06662 -0.77847,2.06243 -1.3635,2.9875 -0.58503,0.925 -1.28703,1.76669 -2.106,2.525 -0.8189,0.75831 -1.728,1.40838 -2.727,1.95 -0.99908,0.54169 -2.07447,0.9625 -3.22658,1.2625 -1.15195,0.3 -2.34892,0.45 -3.59092,0.45 z m 8.289,-16.025 -2.16,-2.025 c -0.072,-0.0667 -0.17097,-0.1 -0.29692,-0.1 -0.12603,0 -0.22505,0.0333 -0.297,0.1 l -8.47808,7.85 -2.592,-2.425 c -0.19797,-0.15 -0.39603,-0.15 -0.594,0 l -2.16,2.025 c -0.072,0.0667 -0.108,0.15831 -0.108,0.275 0,0.1 0.036,0.18331 0.108,0.25 l 5.049,4.675 c 0.09,0.0833 0.189,0.12507 0.297,0.12507 l 0.027,0 c 0.12603,0 0.216,-0.0417 0.27,-0.12507 l 10.935,-10.1 c 0.09,-0.0833 0.13508,-0.175 0.13508,-0.275 -8e-5,-0.1 -0.0451,-0.18331 -0.13508,-0.25 z"
		id="path9898" />
    
	<text
		xml:space="preserve"
		style="font-style:normal;font-weight:normal;font-size:27.5px;
			line-height:125%;font-family:sans-serif;letter-spacing:0px;
			word-spacing:0px;fill:#b3b3b3;fill-opacity:1;stroke:none;
			stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;
			stroke-opacity:1"
		x="218.9921"
		y="174.3622"
		id="text9842"
		sodipodi:linespacing="125%">
		<tspan
			sodipodi:role="line"
			id="tspan9844"
			x="218.9921"
			y="174.3622"
			style="font-style:normal;font-variant:normal;
				font-weight:normal;font-stretch:normal;
				font-size:25px;font-family:Utopia;
				-inkscape-font-specification:Utopia;
				fill:#b3b3b3;fill-opacity:1">DOI
		</tspan>
	</text>
	"""

	box_second = """
	<rect
		style="fill:#b3b3b3;fill-opacity:1;stroke:none;stroke-width:2;
			stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
		id="rect9652-6"
		width="321.60416"
		height="36.53516"
		x="143.8214"
		y="-229.27432"
		transform="scale(1,-1)"
		ry="5.3032908" />    
	<rect
		style="fill:#ffffff"
		id="rect3372-2"
		width="340.75"
		height="30"
		x="121.49999"
		y="196.11221"
		ry="3.8691864" />

    
	<path
		inkscape:connector-curvature="0"
		style="fill:#b3b3b3;fill-opacity:1"
		d="m 200.01934,223.40513 c -1.242,0 -2.43897,-0.15 -3.591,-0.45 -1.15203,-0.30007 -2.2275,-0.72081 -3.2265,-1.2625 -0.999,-0.54169 -1.90803,-1.19169 -2.727,-1.95 -0.81897,-0.75824 -1.52097,-1.6 -2.106,-2.525 -0.58503,-0.92507 -1.0395,-1.92081 -1.3635,-2.9875 -0.324,-1.06669 -0.486,-2.175 -0.486,-3.325 0,-1.15 0.162,-2.25831 0.486,-3.325 0.324,-1.06669 0.77847,-2.0625 1.3635,-2.9875 0.58503,-0.925 1.28703,-1.76669 2.106,-2.525 0.81897,-0.7583 1.728,-1.4083 2.727,-1.94999 0.999,-0.5417 2.07447,-0.9625 3.2265,-1.2625 1.15203,-0.3 2.349,-0.45 3.591,-0.45 1.85403,0 3.6045,0.32919 5.2515,0.9875 1.647,0.6583 3.078,1.55 4.293,2.67499 1.215,1.125 2.17803,2.45 2.889,3.975 0.71097,1.525 1.0665,3.14581 1.0665,4.8625 0,1.15 -0.162,2.25831 -0.486,3.325 -0.32408,1.06662 -0.77847,2.06243 -1.3635,2.9875 -0.58503,0.925 -1.28703,1.76669 -2.106,2.525 -0.8189,0.75831 -1.728,1.40838 -2.727,1.95 -0.99908,0.54169 -2.07447,0.9625 -3.22658,1.2625 -1.15195,0.3 -2.34892,0.45 -3.59092,0.45 z m 8.289,-16.025 -2.16,-2.025 c -0.072,-0.0667 -0.17097,-0.1 -0.29692,-0.1 -0.12603,0 -0.22505,0.0333 -0.297,0.1 l -8.47808,7.85 -2.592,-2.425 c -0.19797,-0.15 -0.39603,-0.15 -0.594,0 l -2.16,2.025 c -0.072,0.0667 -0.108,0.15831 -0.108,0.275 0,0.1 0.036,0.18331 0.108,0.25 l 5.049,4.675 c 0.09,0.0833 0.189,0.12507 0.297,0.12507 l 0.027,0 c 0.12603,0 0.216,-0.0417 0.27,-0.12507 l 10.935,-10.1 c 0.09,-0.0833 0.13508,-0.175 0.13508,-0.275 -8e-5,-0.1 -0.0451,-0.18331 -0.13508,-0.25 z"
		id="path9898-6" />
    
	<text
		xml:space="preserve"
		style="font-style:normal;font-weight:normal;font-size:30px;
			line-height:125%;font-family:sans-serif;letter-spacing:0px;
			word-spacing:0px;fill:#b3b3b3;fill-opacity:1;stroke:none;
			stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;
			stroke-opacity:1"
		x="218.9921"
		y="219.99225"
		id="text9842-6"
		sodipodi:linespacing="125%">
		<tspan
			sodipodi:role="line"
			id="tspan9844-3"
			x="218.9921"
			y="219.99225"
			style="font-style:normal;font-variant:normal;
				font-weight:normal;font-stretch:normal;
				font-size:25px;font-family:Utopia;
				-inkscape-font-specification:Utopia;fill:#b3b3b3;
				fill-opacity:1">DOCUMENTATION
		</tspan>
	</text>
	"""

	box_third = """
	<rect
		style="fill:#b3b3b3;fill-opacity:1;stroke:none;stroke-width:2;
			stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
		id="rect9652-0"
		width="293.06238"
		height="36.13789"
		x="172.36316"
		y="-273.41672"
		transform="scale(1,-1)"
		ry="6.1871843" />
	<rect
		style="fill:#ffffff"
		id="rect3372-7"
		width="340.75"
		height="30"
		x="121.49999"
		y="-270.323"
		ry="3.8691864"
		transform="scale(1,-1)" />

    
	<path
		inkscape:connector-curvature="0"
		style="fill:#b3b3b3;fill-opacity:1"
		d="m 200.01934,268.65997 c -1.242,0 -2.43897,-0.15 -3.591,-0.45 -1.15203,-0.30007 -2.2275,-0.72081 -3.2265,-1.2625 -0.999,-0.54169 -1.90803,-1.19169 -2.727,-1.95 -0.81897,-0.75824 -1.52097,-1.6 -2.106,-2.525 -0.58503,-0.92507 -1.0395,-1.92081 -1.3635,-2.9875 -0.324,-1.06669 -0.486,-2.175 -0.486,-3.325 0,-1.15 0.162,-2.25831 0.486,-3.325 0.324,-1.06669 0.77847,-2.0625 1.3635,-2.9875 0.58503,-0.925 1.28703,-1.76669 2.106,-2.525 0.81897,-0.7583 1.728,-1.4083 2.727,-1.94999 0.999,-0.5417 2.07447,-0.9625 3.2265,-1.2625 1.15203,-0.3 2.349,-0.45 3.591,-0.45 1.85403,0 3.6045,0.32919 5.2515,0.9875 1.647,0.6583 3.078,1.55 4.293,2.67499 1.215,1.125 2.17803,2.45 2.889,3.975 0.71097,1.525 1.0665,3.14581 1.0665,4.8625 0,1.15 -0.162,2.25831 -0.486,3.325 -0.32408,1.06662 -0.77847,2.06243 -1.3635,2.9875 -0.58503,0.925 -1.28703,1.76669 -2.106,2.525 -0.8189,0.75831 -1.728,1.40838 -2.727,1.95 -0.99908,0.54169 -2.07447,0.9625 -3.22658,1.2625 -1.15195,0.3 -2.34892,0.45 -3.59092,0.45 z m 8.289,-16.025 -2.16,-2.025 c -0.072,-0.0667 -0.17097,-0.1 -0.29692,-0.1 -0.12603,0 -0.22505,0.0333 -0.297,0.1 l -8.47808,7.85 -2.592,-2.425 c -0.19797,-0.15 -0.39603,-0.15 -0.594,0 l -2.16,2.025 c -0.072,0.0667 -0.108,0.15831 -0.108,0.275 0,0.1 0.036,0.18331 0.108,0.25 l 5.049,4.675 c 0.09,0.0833 0.189,0.12507 0.297,0.12507 l 0.027,0 c 0.12603,0 0.216,-0.0417 0.27,-0.12507 l 10.935,-10.1 c 0.09,-0.0833 0.13508,-0.175 0.13508,-0.275 -8e-5,-0.1 -0.0451,-0.18331 -0.13508,-0.25 z"
		id="path9898-5" />
    
	<text
		xml:space="preserve"
		style="font-style:normal;font-weight:normal;font-size:30px;
			line-height:125%;font-family:sans-serif;letter-spacing:0px;
			word-spacing:0px;fill:#b3b3b3;fill-opacity:1;stroke:none;
			stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;
			stroke-opacity:1"
		x="218.60208"
		y="265.12576"
		id="text9842-2"
		sodipodi:linespacing="125%">
		<tspan
			sodipodi:role="line"
			id="tspan9844-5"
			x="218.60208"
			y="265.12576"
			style="font-style:normal;font-variant:normal;
				font-weight:normal;font-stretch:normal;
				font-size:25px;font-family:Utopia;
				-inkscape-font-specification:Utopia;fill:#b3b3b3;
				fill-opacity:1">CONTACT INFO
		</tspan>
	</text>
	"""

	box_fourth = """
	<rect
		style="fill:#b3b3b3;fill-opacity:1;stroke:none;stroke-width:2;
			stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
		id="rect9652-2"
		width="331.45035"
		height="36.53516"
		x="133.97522"
		y="-318.35361"
		transform="scale(1,-1)"
		ry="5.3033009" />
            
	<rect
		style="fill:#ffffff"
		id="rect3372-5"
		width="340.75"
		height="30"
		x="121.49999"
		y="-314.86218"
		ry="3.8691864"
		transform="scale(1,-1)" />

    
	<path
		inkscape:connector-curvature="0"
		style="fill:#b3b3b3;fill-opacity:1"
		d="m 200.01934,311.08638 c -1.242,0 -2.43897,-0.15 -3.591,-0.45 -1.15203,-0.30007 -2.2275,-0.72081 -3.2265,-1.2625 -0.999,-0.54169 -1.90803,-1.19169 -2.727,-1.95 -0.81897,-0.75824 -1.52097,-1.6 -2.106,-2.525 -0.58503,-0.92507 -1.0395,-1.92081 -1.3635,-2.9875 -0.324,-1.06669 -0.486,-2.175 -0.486,-3.325 0,-1.15 0.162,-2.25831 0.486,-3.325 0.324,-1.06669 0.77847,-2.0625 1.3635,-2.9875 0.58503,-0.925 1.28703,-1.76669 2.106,-2.525 0.81897,-0.7583 1.728,-1.4083 2.727,-1.94999 0.999,-0.5417 2.07447,-0.9625 3.2265,-1.2625 1.15203,-0.3 2.349,-0.45 3.591,-0.45 1.85403,0 3.6045,0.32919 5.2515,0.9875 1.647,0.6583 3.078,1.55 4.293,2.67499 1.215,1.125 2.17803,2.45 2.889,3.975 0.71097,1.525 1.0665,3.14581 1.0665,4.8625 0,1.15 -0.162,2.25831 -0.486,3.325 -0.32408,1.06662 -0.77847,2.06243 -1.3635,2.9875 -0.58503,0.925 -1.28703,1.76669 -2.106,2.525 -0.8189,0.75831 -1.728,1.40838 -2.727,1.95 -0.99908,0.54169 -2.07447,0.9625 -3.22658,1.2625 -1.15195,0.3 -2.34892,0.45 -3.59092,0.45 z m 8.289,-16.025 -2.16,-2.025 c -0.072,-0.0667 -0.17097,-0.1 -0.29692,-0.1 -0.12603,0 -0.22505,0.0333 -0.297,0.1 l -8.47808,7.85 -2.592,-2.425 c -0.19797,-0.15 -0.39603,-0.15 -0.594,0 l -2.16,2.025 c -0.072,0.0667 -0.108,0.15831 -0.108,0.275 0,0.1 0.036,0.18331 0.108,0.25 l 5.049,4.675 c 0.09,0.0833 0.189,0.12507 0.297,0.12507 l 0.027,0 c 0.12603,0 0.216,-0.0417 0.27,-0.12507 l 10.935,-10.1 c 0.09,-0.0833 0.13508,-0.175 0.13508,-0.275 -8e-5,-0.1 -0.0451,-0.18331 -0.13508,-0.25 z"
		id="path9898-9" />
    
	<text
		xml:space="preserve"
		style="font-style:normal;font-variant:normal;font-weight:500;
			font-stretch:normal;font-size:40px;line-height:125%;
			font-family:'Type Embellishments One LET';
			-inkscape-font-specification:'Type Embellishments One 
			LET Medium';letter-spacing:0px;word-spacing:0px;
			fill:#000000;fill-opacity:1;stroke:none;stroke-width:1px;
			stroke-linecap:butt;stroke-linejoin:miter;stroke-opacity:1"
		x="185"
		y="163.3622"
		id="text9846"
		sodipodi:linespacing="125%"><tspan
		sodipodi:role="line"
		id="tspan9848"
		x="185"
		y="163.3622"
		style="font-style:normal;font-variant:normal;font-weight:normal;
			font-stretch:normal;font-family:Wingdings;
			-inkscape-font-specification:Wingdings" />
	</text>
    
	<text
		xml:space="preserve"
		style="font-style:normal;font-weight:normal;font-size:30px;
			line-height:125%;font-family:sans-serif;letter-spacing:0px;
			word-spacing:0px;fill:#b3b3b3;fill-opacity:1;stroke:none;
			stroke-width:1px;stroke-linecap:butt;stroke-linejoin:miter;
			stroke-opacity:1"
		x="218.9921"
		y="307.55215"
		id="text9842-7"
		sodipodi:linespacing="125%">
		<tspan
			sodipodi:role="line"
			id="tspan9844-1"
			x="218.9921"
			y="307.55215"
			style="font-style:normal;font-variant:normal;
				font-weight:normal;font-stretch:normal;
				font-size:25px;font-family:Utopia;
				-inkscape-font-specification:Utopia;fill:#b3b3b3;
				fill-opacity:1">LICENSE (MIT)
		</tspan>
	</text>

	"""

	# importante el cierre
	remaining = """
	<g
		transform="matrix(1.25,0,0,-1.25,411.09563,460.5664)"
		id="g3789" />
	"""
	
	footer = """
	</g>
	</svg>
	"""

	image = header 

	if (license != None):
		image += box_fourth
		image += color_fourth

	if (contact != False):
		image += box_third
		image += color_third

	if (documentation != False):
		image += box_second
		image += color_second

	if (doi != None): 
		image += box_first
		image += color_first

	image += border
	image += footer

	return image


if __name__ == "__main__":
    main()

