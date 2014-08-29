/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

//;window.Modernizr=function(a,b,c){function z(a){j.cssText=a}function A(a,b){return z(m.join(a+";")+(b||""))}function B(a,b){return typeof a===b}function C(a,b){return!!~(""+a).indexOf(b)}function D(a,b){for(var d in a){var e=a[d];if(!C(e,"-")&&j[e]!==c)return b=="pfx"?e:!0}return!1}function E(a,b,d){for(var e in a){var f=b[a[e]];if(f!==c)return d===!1?a[e]:B(f,"function")?f.bind(d||b):f}return!1}function F(a,b,c){var d=a.charAt(0).toUpperCase()+a.slice(1),e=(a+" "+o.join(d+" ")+d).split(" ");return B(b,"string")||B(b,"undefined")?D(e,b):(e=(a+" "+p.join(d+" ")+d).split(" "),E(e,b,c))}var d="2.6.2",e={},f=!0,g=b.documentElement,h="modernizr",i=b.createElement(h),j=i.style,k,l={}.toString,m=" -webkit- -moz- -o- -ms- ".split(" "),n="Webkit Moz O ms",o=n.split(" "),p=n.toLowerCase().split(" "),q={},r={},s={},t=[],u=t.slice,v,w=function(a,c,d,e){var f,i,j,k,l=b.createElement("div"),m=b.body,n=m||b.createElement("body");if(parseInt(d,10))while(d--)j=b.createElement("div"),j.id=e?e[d]:h+(d+1),l.appendChild(j);return f=["&#173;",'<style id="s',h,'">',a,"</style>"].join(""),l.id=h,(m?l:n).innerHTML+=f,n.appendChild(l),m||(n.style.background="",n.style.overflow="hidden",k=g.style.overflow,g.style.overflow="hidden",g.appendChild(n)),i=c(l,a),m?l.parentNode.removeChild(l):(n.parentNode.removeChild(n),g.style.overflow=k),!!i},x={}.hasOwnProperty,y;!B(x,"undefined")&&!B(x.call,"undefined")?y=function(a,b){return x.call(a,b)}:y=function(a,b){return b in a&&B(a.constructor.prototype[b],"undefined")},Function.prototype.bind||(Function.prototype.bind=function(b){var c=this;if(typeof c!="function")throw new TypeError;var d=u.call(arguments,1),e=function(){if(this instanceof e){var a=function(){};a.prototype=c.prototype;var f=new a,g=c.apply(f,d.concat(u.call(arguments)));return Object(g)===g?g:f}return c.apply(b,d.concat(u.call(arguments)))};return e}),q.touch=function(){var c;return"ontouchstart"in a||a.DocumentTouch&&b instanceof DocumentTouch?c=!0:w(["@media (",m.join("touch-enabled),("),h,")","{#modernizr{top:9px;position:absolute}}"].join(""),function(a){c=a.offsetTop===9}),c},q.csstransforms3d=function(){var a=!!F("perspective");return a&&"webkitPerspective"in g.style&&w("@media (transform-3d),(-webkit-transform-3d){#modernizr{left:9px;position:absolute;height:3px;}}",function(b,c){a=b.offsetLeft===9&&b.offsetHeight===3}),a},q.csstransitions=function(){return F("transition")};for(var G in q)y(q,G)&&(v=G.toLowerCase(),e[v]=q[G](),t.push((e[v]?"":"no-")+v));return e.addTest=function(a,b){if(typeof a=="object")for(var d in a)y(a,d)&&e.addTest(d,a[d]);else{a=a.toLowerCase();if(e[a]!==c)return e;b=typeof b=="function"?b():b,typeof f!="undefined"&&f&&(g.className+=" "+(b?"":"no-")+a),e[a]=b}return e},z(""),i=k=null,function(a,b){function k(a,b){var c=a.createElement("p"),d=a.getElementsByTagName("head")[0]||a.documentElement;return c.innerHTML="x<style>"+b+"</style>",d.insertBefore(c.lastChild,d.firstChild)}function l(){var a=r.elements;return typeof a=="string"?a.split(" "):a}function m(a){var b=i[a[g]];return b||(b={},h++,a[g]=h,i[h]=b),b}function n(a,c,f){c||(c=b);if(j)return c.createElement(a);f||(f=m(c));var g;return f.cache[a]?g=f.cache[a].cloneNode():e.test(a)?g=(f.cache[a]=f.createElem(a)).cloneNode():g=f.createElem(a),g.canHaveChildren&&!d.test(a)?f.frag.appendChild(g):g}function o(a,c){a||(a=b);if(j)return a.createDocumentFragment();c=c||m(a);var d=c.frag.cloneNode(),e=0,f=l(),g=f.length;for(;e<g;e++)d.createElement(f[e]);return d}function p(a,b){b.cache||(b.cache={},b.createElem=a.createElement,b.createFrag=a.createDocumentFragment,b.frag=b.createFrag()),a.createElement=function(c){return r.shivMethods?n(c,a,b):b.createElem(c)},a.createDocumentFragment=Function("h,f","return function(){var n=f.cloneNode(),c=n.createElement;h.shivMethods&&("+l().join().replace(/\w+/g,function(a){return b.createElem(a),b.frag.createElement(a),'c("'+a+'")'})+");return n}")(r,b.frag)}function q(a){a||(a=b);var c=m(a);return r.shivCSS&&!f&&!c.hasCSS&&(c.hasCSS=!!k(a,"article,aside,figcaption,figure,footer,header,hgroup,nav,section{display:block}mark{background:#FF0;color:#000}")),j||p(a,c),a}var c=a.html5||{},d=/^<|^(?:button|map|select|textarea|object|iframe|option|optgroup)$/i,e=/^(?:a|b|code|div|fieldset|h1|h2|h3|h4|h5|h6|i|label|li|ol|p|q|span|strong|style|table|tbody|td|th|tr|ul)$/i,f,g="_html5shiv",h=0,i={},j;(function(){try{var a=b.createElement("a");a.innerHTML="<xyz></xyz>",f="hidden"in a,j=a.childNodes.length==1||function(){b.createElement("a");var a=b.createDocumentFragment();return typeof a.cloneNode=="undefined"||typeof a.createDocumentFragment=="undefined"||typeof a.createElement=="undefined"}()}catch(c){f=!0,j=!0}})();var r={elements:c.elements||"abbr article aside audio bdi canvas data datalist details figcaption figure footer header hgroup mark meter nav output progress section summary time video",shivCSS:c.shivCSS!==!1,supportsUnknownElements:j,shivMethods:c.shivMethods!==!1,type:"default",shivDocument:q,createElement:n,createDocumentFragment:o};a.html5=r,q(b)}(this,b),e._version=d,e._prefixes=m,e._domPrefixes=p,e._cssomPrefixes=o,e.testProp=function(a){return D([a])},e.testAllProps=F,e.testStyles=w,e.prefixed=function(a,b,c){return b?F(a,b,c):F(a,"pfx")},g.className=g.className.replace(/(^|\s)no-js(\s|$)/,"$1$2")+(f?" js "+t.join(" "):""),e}(this,this.document),function(a,b,c){function d(a){return"[object Function]"==o.call(a)}function e(a){return"string"==typeof a}function f(){}function g(a){return!a||"loaded"==a||"complete"==a||"uninitialized"==a}function h(){var a=p.shift();q=1,a?a.t?m(function(){("c"==a.t?B.injectCss:B.injectJs)(a.s,0,a.a,a.x,a.e,1)},0):(a(),h()):q=0}function i(a,c,d,e,f,i,j){function k(b){if(!o&&g(l.readyState)&&(u.r=o=1,!q&&h(),l.onload=l.onreadystatechange=null,b)){"img"!=a&&m(function(){t.removeChild(l)},50);for(var d in y[c])y[c].hasOwnProperty(d)&&y[c][d].onload()}}var j=j||B.errorTimeout,l=b.createElement(a),o=0,r=0,u={t:d,s:c,e:f,a:i,x:j};1===y[c]&&(r=1,y[c]=[]),"object"==a?l.data=c:(l.src=c,l.type=a),l.width=l.height="0",l.onerror=l.onload=l.onreadystatechange=function(){k.call(this,r)},p.splice(e,0,u),"img"!=a&&(r||2===y[c]?(t.insertBefore(l,s?null:n),m(k,j)):y[c].push(l))}function j(a,b,c,d,f){return q=0,b=b||"j",e(a)?i("c"==b?v:u,a,b,this.i++,c,d,f):(p.splice(this.i++,0,a),1==p.length&&h()),this}function k(){var a=B;return a.loader={load:j,i:0},a}var l=b.documentElement,m=a.setTimeout,n=b.getElementsByTagName("script")[0],o={}.toString,p=[],q=0,r="MozAppearance"in l.style,s=r&&!!b.createRange().compareNode,t=s?l:n.parentNode,l=a.opera&&"[object Opera]"==o.call(a.opera),l=!!b.attachEvent&&!l,u=r?"object":l?"script":"img",v=l?"script":u,w=Array.isArray||function(a){return"[object Array]"==o.call(a)},x=[],y={},z={timeout:function(a,b){return b.length&&(a.timeout=b[0]),a}},A,B;B=function(a){function b(a){var a=a.split("!"),b=x.length,c=a.pop(),d=a.length,c={url:c,origUrl:c,prefixes:a},e,f,g;for(f=0;f<d;f++)g=a[f].split("="),(e=z[g.shift()])&&(c=e(c,g));for(f=0;f<b;f++)c=x[f](c);return c}function g(a,e,f,g,h){var i=b(a),j=i.autoCallback;i.url.split(".").pop().split("?").shift(),i.bypass||(e&&(e=d(e)?e:e[a]||e[g]||e[a.split("/").pop().split("?")[0]]),i.instead?i.instead(a,e,f,g,h):(y[i.url]?i.noexec=!0:y[i.url]=1,f.load(i.url,i.forceCSS||!i.forceJS&&"css"==i.url.split(".").pop().split("?").shift()?"c":c,i.noexec,i.attrs,i.timeout),(d(e)||d(j))&&f.load(function(){k(),e&&e(i.origUrl,h,g),j&&j(i.origUrl,h,g),y[i.url]=2})))}function h(a,b){function c(a,c){if(a){if(e(a))c||(j=function(){var a=[].slice.call(arguments);k.apply(this,a),l()}),g(a,j,b,0,h);else if(Object(a)===a)for(n in m=function(){var b=0,c;for(c in a)a.hasOwnProperty(c)&&b++;return b}(),a)a.hasOwnProperty(n)&&(!c&&!--m&&(d(j)?j=function(){var a=[].slice.call(arguments);k.apply(this,a),l()}:j[n]=function(a){return function(){var b=[].slice.call(arguments);a&&a.apply(this,b),l()}}(k[n])),g(a[n],j,b,n,h))}else!c&&l()}var h=!!a.test,i=a.load||a.both,j=a.callback||f,k=j,l=a.complete||f,m,n;c(h?a.yep:a.nope,!!i),i&&c(i)}var i,j,l=this.yepnope.loader;if(e(a))g(a,0,l,0);else if(w(a))for(i=0;i<a.length;i++)j=a[i],e(j)?g(j,0,l,0):w(j)?B(j):Object(j)===j&&h(j,l);else Object(a)===a&&h(a,l)},B.addPrefix=function(a,b){z[a]=b},B.addFilter=function(a){x.push(a)},B.errorTimeout=1e4,null==b.readyState&&b.addEventListener&&(b.readyState="loading",b.addEventListener("DOMContentLoaded",A=function(){b.removeEventListener("DOMContentLoaded",A,0),b.readyState="complete"},0)),a.yepnope=k(),a.yepnope.executeStack=h,a.yepnope.injectJs=function(a,c,d,e,i,j){var k=b.createElement("script"),l,o,e=e||B.errorTimeout;k.src=a;for(o in d)k.setAttribute(o,d[o]);c=j?h:c||f,k.onreadystatechange=k.onload=function(){!l&&g(k.readyState)&&(l=1,c(),k.onload=k.onreadystatechange=null)},m(function(){l||(l=1,c(1))},e),i?k.onload():n.parentNode.insertBefore(k,n)},a.yepnope.injectCss=function(a,c,d,e,g,i){var e=b.createElement("link"),j,c=i?h:c||f;e.href=a,e.rel="stylesheet",e.type="text/css";for(j in d)e.setAttribute(j,d[j]);g||(n.parentNode.insertBefore(e,n),m(c,0))}}(this,document),Modernizr.load=function(){yepnope.apply(window,[].slice.call(arguments,0))};

;( function( $, window, undefined ) {
	
	'use strict';

	/*
	* debouncedresize: special jQuery event that happens once after a window resize
	*
	* latest version and complete README available on Github:
	* https://github.com/louisremi/jquery-smartresize/blob/master/jquery.debouncedresize.js
	*
	* Copyright 2011 @louis_remi
	* Licensed under the MIT license.
	*/
	var $event = $.event,
	$special,
	resizeTimeout;

	$special = $event.special.debouncedresize = {
		setup: function() {
			$( this ).on( "resize", $special.handler );
		},
		teardown: function() {
			$( this ).off( "resize", $special.handler );
		},
		handler: function( event, execAsap ) {
			// Save the context
			var context = this,
				args = arguments,
				dispatch = function() {
					// set correct event type
					event.type = "debouncedresize";
					$event.dispatch.apply( context, args );
				};

			if ( resizeTimeout ) {
				clearTimeout( resizeTimeout );
			}

			execAsap ?
				dispatch() :
				resizeTimeout = setTimeout( dispatch, $special.threshold );
		},
		threshold: 50
	};

	// global
	var $window = $( window ),
		Modernizr = window.Modernizr;

	$.PFold = function( options, element ) {
		
		this.$el = $( element );
		this._init( options );
		
	};

	// the options
	$.PFold.defaults = {
		// perspective value
		perspective : 1200,
		// each folding step's speed
		speed : 450,
		// each folding step's easing 
		easing : 'linear',
		// delay between each (un)folding step (ms)
		folddelay : 0,
		// number of times the element will fold
		folds : 2,
		// the direction of each unfolding step
		folddirection : ['right','top'],
		// use overlays to simulate a shadow for each folding step 
		overlays : true,
		// the main container moves (translation) in order to keep its initial position 
		centered : false,
		// allows us to specify a different speed for the container's translation
		// values range : [0 - 1] 
		// if 0 the container jumps immediately to the final position (translation).
		// this is only valid if centered is true
		containerSpeedFactor : 1,
		// easing for the container transition
		// this is only valid if centered is true
		containerEasing : 'linear',
		// callbacks
		onEndFolding : function() { return false; },
		onEndUnfolding : function() { return false; }
	};

	$.PFold.prototype = {

		_init : function( options ) {
			
			// options
			this.options = $.extend( true, {}, $.PFold.defaults, options );

			// https://github.com/twitter/bootstrap/issues/2870
			this.transEndEventNames = {
				'WebkitTransition' : 'webkitTransitionEnd',
				'MozTransition' : 'transitionend',
				'OTransition' : 'oTransitionEnd',
				'msTransition' : 'MSTransitionEnd',
				'transition' : 'transitionend'
			};
			this.transEndEventName = this.transEndEventNames[ Modernizr.prefixed( 'transition' ) ];

			// suport for css 3d transforms and css transitions
			this.support = Modernizr.csstransitions && Modernizr.csstransforms3d;

			// apply perspective to the main container
			if( this.support ) {

				this.$el.css( 'perspective', this.options.perspective + 'px' );
				
				// set the transition to the main container
				// we will need to move it if:
				// this.options.centered is true;
				// the opened element goes outside of the viewport
				this.$el.css( 'transition', 'all ' + ( this.options.speed * this.options.folds * this.options.containerSpeedFactor ) + 'ms ' + this.options.containerEasing );

			}

			// initial sizes
			this.initialDim = {
				width : this.$el.width(),
				height : this.$el.height(),
				left : 0,
				top : 0
			};

			// change the layout
			this._layout();

			// cache some initial values:
			// initial content
			this.$iContent = this.$el.find( '.uc-initial' );
			this.iContent = this.$iContent.html();
			// final content
			this.$fContent = this.$el.find( '.uc-final' );
			this.fContent = this.$fContent.html();
			// this element is inserted in the main container and it will contain the initial and final content elements
			this.$finalEl = $( '<div class="uc-final-wrapper"></div>' ).append( this.$iContent.clone().hide(), this.$fContent ).hide();
			this.$el.append( this.$finalEl );
			
			// initial element's offset
			this._setDimOffset();

			// status
			this.opened = false;
			this.animating = false;
			
			// initialize events
			this._initEvents();

		},
		// changes the initial html structure
		// adds wrappers to the uc-initial-content and uc-final-content divs
		_layout : function() {

			var $initialContentEl = this.$el.children( 'div.uc-initial-content' ),
				finalDim = this._getFinalDim(),
				$finalContentEl = this.$el.children( 'div.uc-final-content' ).css( {
					width : finalDim.width,
					height : finalDim.height
				} );

			$initialContentEl.wrap( '<div class="uc-initial"></div>' );
			$finalContentEl.show().wrap( $( '<div class="uc-final"></div>' ) );

		},
		// initialize the necessary events
		_initEvents : function() {

			var self = this;

			$window.on( 'debouncedresize.pfold', function( event ) {

				// update offsets
				self._setDimOffset();
				
			} );

		},
		// set/update offsets
		_setDimOffset : function() {

			this.initialDim.offsetL = this.$el.offset().left - $window.scrollLeft();
			this.initialDim.offsetT = this.$el.offset().top - $window.scrollTop();
			this.initialDim.offsetR = $window.width() - this.initialDim.offsetL - this.initialDim.width;
			this.initialDim.offsetB = $window.height() - this.initialDim.offsetT - this.initialDim.height;

		},
		// gets the values needed to translate the main container (if options.centered is true)
		_getTranslationValue : function() {

			var x = 0, 
				y = 0,
				horizTimes = 0,
				vertTimes = 0;

			for( var i = 0; i < this.options.folds; ++i ) {

				// bottom as default
				var dir = this.options.folddirection[ i ] || 'bottom';

				switch( dir ) {

					case 'left' :

						x += this.initialDim.width * Math.pow( 2, horizTimes ) / 2;
						horizTimes += 1;
						break;

					case 'right' :

						x -= this.initialDim.width * Math.pow( 2, horizTimes ) / 2;
						horizTimes += 1;
						break;

					case 'top' :

						y += this.initialDim.height * Math.pow( 2, vertTimes ) / 2;
						vertTimes += 1;
						break;

					case 'bottom' :

						y -= this.initialDim.height * Math.pow( 2, vertTimes ) / 2;
						vertTimes += 1;
						break;
				
				}

			}

			return {
				x : x,
				y : y
			};

		},
		// gets the accumulated values for left, right, top and bottom once the element is opened
		_getAccumulatedValue : function() {

			var l = 0, 
				r = 0,
				t = 0, 
				b = 0,
				horizTimes = 0,
				vertTimes = 0;

			for( var i = 0; i < this.options.folds; ++i ) {

				// bottom as default
				var dir = this.options.folddirection[ i ] || 'bottom';

				switch( dir ) {

					case 'left' :

						l += this.initialDim.width * Math.pow( 2, horizTimes );
						horizTimes += 1;
						break;

					case 'right' :

						r += this.initialDim.width * Math.pow( 2, horizTimes );
						horizTimes += 1;
						break;

					case 'top' :

						t += this.initialDim.height * Math.pow( 2, vertTimes );
						vertTimes += 1;
						break;

					case 'bottom' :

						b += this.initialDim.height * Math.pow( 2, vertTimes );
						vertTimes += 1;
						break;
				
				}

			}

			return {
				l : l,
				r : r,
				t : t,
				b : b
			};

		},
		// gets the width and height of the element when it is opened
		_getFinalDim : function() {

			var l = 0, 
				r = 0,
				t = 0, 
				b = 0,
				horizTimes = 0,
				vertTimes = 0;

			for( var i = 0; i < this.options.folds; ++i ) {

				// bottom as default
				var dir = this.options.folddirection[ i ] || 'bottom';

				switch( dir ) {

					case 'left' : case 'right' :

						horizTimes += 1;
						break;

					case 'top' : case 'bottom' :

						vertTimes += 1;
						break;
				
				}

			}

			return {
				width : this.initialDim.width * Math.pow( 2, horizTimes ),
				height : this.initialDim.height * Math.pow( 2, vertTimes )
			};

		},
		// returns the sizes and positions for the element after each (un)folding step
		_updateStepStyle : function( action ) {

			var w, h, l, t;

			if( action === 'fold' ) {

				w = this.lastDirection === 'left' || this.lastDirection === 'right' ? this.lastStyle.width / 2 : this.lastStyle.width,
				h = this.lastDirection === 'left' || this.lastDirection === 'right' ? this.lastStyle.height : this.lastStyle.height / 2,
				l = this.lastDirection === 'left' ? this.lastStyle.left + this.lastStyle.width / 2 : this.lastStyle.left,
				t = this.lastDirection === 'top' ? this.lastStyle.top + this.lastStyle.height / 2  : this.lastStyle.top;

			}
			else {

				w = this.lastDirection === 'left' || this.lastDirection === 'right' ? this.lastStyle.width * 2 : this.lastStyle.width,
				h = this.lastDirection === 'left' || this.lastDirection === 'right' ? this.lastStyle.height : this.lastStyle.height * 2,
				l = this.lastDirection === 'left' ? this.lastStyle.left - this.lastStyle.width : this.lastStyle.left,
				t = this.lastDirection === 'top' ? this.lastStyle.top - this.lastStyle.height : this.lastStyle.top;	

			}

			return {
				width : w,
				height : h,
				left : l,
				top : t
			};

		},
		// get the opposite direction
		_getOppositeDirection : function( realdirection ) {

			var rvd;

			switch( realdirection ) {

				case 'left' : rvd = 'right'; break;
				case 'right' : rvd = 'left'; break;
				case 'top' : rvd = 'bottom'; break;
				case 'bottom' : rvd = 'top'; break;

			}

			return rvd;

		},
		// main function: unfolds and folds the element [options.folds] times by using recursive calls
		_start : function( action, step ) {

			// Basically we are replacing the element's content with 2 divisions, the top and bottom elements.
			// The top element will have a front and back faces. The front has the initial content for the first step
			// and the back will have the final content for the last step. For all the other cases the top element will be blank.
			// The bottom element will have the final content for the last step and will be blank for all the other cases.
			// We need to keep the right sizes and positions for these 2 elements, so we need to cache the previous step's state.

			step |= 0;
			
			var self = this,
				styleCSS = ( action === 'fold' ) ? {
					width : this.lastStyle.width,
					height : this.lastStyle.height,
					left : this.lastStyle.left,
					top : this.lastStyle.top
				} : this.initialDim,
				contentTopFront = '', contentBottom = '', contentTopBack = '',
				// direction for step [step]
				// bottom is the default value if none is present
				direction = ( action === 'fold' ) ?
					this.options.folddirection[ this.options.folds - 1 - step ] || 'bottom' :
					this.options.folddirection[ step ] || 'bottom',
				// future direction value (only for the "fold" action)
				nextdirection = ( action === 'fold' ) ? this.options.folddirection[ this.options.folds - 2 - step ] || 'bottom' : '';

			// remove uc-part divs inside the container (the top and bottom elements)
			this.$el.find( 'div.uc-part' ).remove();

			switch( step ) {

				// first step & last transition step
				case 0 : case this.options.folds - 1 :

					if( action === 'fold' ) {

						if( step === this.options.folds - 1 ) {

							styleCSS = this.initialDim;
							contentTopFront = this.iContent;

						}

						if( step === 0 ) {

							this._setDimOffset();

							// reset the translation of the main container
							this.$el.css( { left : 0, top : 0 } );

							var content = this._setLastStep( direction, styleCSS ),
								contentBottom = content.bottom,
								contentTopBack = content.top;

							this.$finalEl.hide().children().hide();

						}

					}
					else { // unfolding

						if( step === 0 ) {

							this._setDimOffset();

							// if options.centered is true, we need to center the container.
							// either ways we need to make sure the container does not move outside the viewport.
							// let's get the correct translation values for the container's transition
							var coords = this._getTranslationViewport();

							this.$el.addClass( 'uc-current' ).css( { left : coords.ftx, top : coords.fty } );

							contentTopFront = this.iContent;

							this.$finalEl.hide().children().hide();

						}
						else {

							styleCSS = this._updateStepStyle( action );

						}

						if( step === this.options.folds - 1 ) {

							var content = this._setLastStep( direction, styleCSS ),
								contentBottom = content.bottom,
								contentTopBack = content.top;

						}

					}

					break;

				// last step is to replace the topElement and bottomElement with a division that has the final content
				case this.options.folds :

					styleCSS = ( action === 'fold') ? this.initialDim : this._updateStepStyle( action );

					// remove top and bottom elements
					var contentIdx = ( action === 'fold' ) ? 0 : 1;
					this.$el
						.find( '.uc-part' )
						.remove();

					this.$finalEl.css( styleCSS ).show().children().eq( contentIdx ).show();
					
					this.opened = ( action === 'fold' ) ? false : true;
					this.animating = false;
					// nothing else to do
					if( action === 'fold' ) {

						this.$el.removeClass( 'uc-current' );
						this.options.onEndFolding();

					}
					else {

						this.options.onEndUnfolding();

					}
					return false;

					break;

				// all the other steps
				default :

					// style of new layout will depend on the last step direction
					styleCSS = this._updateStepStyle( action );

					break;

			}

			// transition properties for the step
			if( this.support ) {
				
				styleCSS.transition = 'all ' + this.options.speed + 'ms ' + this.options.easing;
			
			}

			var unfoldClass = 'uc-unfold-' + direction,
				topElClasses = ( action === 'fold' ) ? 'uc-unfold uc-part ' + unfoldClass : 'uc-part ' + unfoldClass,
				$topEl = $( '<div class="' + topElClasses + '"><div class="uc-front">' + contentTopFront + '</div><div class="uc-back">' + contentTopBack + '</div></div>' ).css( styleCSS ),
				$bottomEl = $( '<div class="uc-part uc-single">' + contentBottom + '</div>' ).css( styleCSS );

			// cache last direction and style
			this.lastDirection = ( action === 'fold' ) ? nextdirection : direction;
			this.lastStyle = styleCSS;

			// append new elements
			this.$el.append( $bottomEl, $topEl );

			// add overlays
			if( this.options.overlays && this.support ) {

				this._addOverlays( action, $bottomEl, $topEl );

			}

			setTimeout( function() {

				// apply style
				( action === 'fold' ) ? $topEl.removeClass( 'uc-unfold' ) : $topEl.addClass( 'uc-unfold' );

				if( self.support ) {

					$topEl.on( self.transEndEventName , function(event) {

						if( event.target.className !== 'uc-flipoverlay' && step < self.options.folds ) {

							// goto next step in [options.folddelay] ms
							setTimeout( function() { self._start( action, step + 1 ); }, self.options.folddelay );

						}

					} );

				}
				else {
					
					// goto next step
					self._start( action, step + 1 );

				}

				if( self.options.overlays && self.support ) {

					var bo = ( action === 'fold' ) ? 1 : 0,
						tbo = ( action === 'fold' ) ? .5 : 0,
						tfo = ( action === 'fold' ) ? 0 : .5;

					self.$bottomOverlay.css( 'opacity', bo );
					self.$topBackOverlay.css( 'opacity', tbo );
					self.$topFrontOverlay.css( 'opacity', tfo );

				}
			
			} , 30 );

		},
		// gets the translation values for the container's transition
		_getTranslationViewport : function() {

			// the accumulatedValues stores the left, right, top and bottom increments to the final/opened element relatively to the initial/closed element
			var accumulatedValues = this._getAccumulatedValue(),
				tx = 0,
				ty = 0;

			// the final offsets for the opened element
			this.fOffsetL = this.initialDim.offsetL - accumulatedValues.l;
			this.fOffsetT = this.initialDim.offsetT - accumulatedValues.t;
			this.fOffsetR = this.initialDim.offsetR - accumulatedValues.r;
			this.fOffsetB = this.initialDim.offsetB - accumulatedValues.b;

			if( this.fOffsetL < 0 ) {
				tx = Math.abs( this.fOffsetL );
			}
			if( this.fOffsetT < 0 ) {
				ty = Math.abs( this.fOffsetT );
			}
			if( this.fOffsetR < 0 ) {
				tx -= Math.abs( this.fOffsetR );
			}
			if( this.fOffsetB < 0 ) {
				ty -= Math.abs( this.fOffsetB );
			}

			// final translation values
			var ftx = tx,
				fty = ty;

			if( this.options.centered ) {

				var translationValue = this._getTranslationValue();

				if( translationValue.x > 0 && this.fOffsetR + translationValue.x >= 0 ) {

					ftx = ( this.fOffsetL >= 0 ) ? Math.min( translationValue.x , this.fOffsetR ) : translationValue.x + ( tx - translationValue.x );

				}
				else if( translationValue.x < 0 && this.fOffsetL + translationValue.x >= 0 ) {
                                    
					ftx = ( this.fOffsetR >= 0 ) ? Math.min( translationValue.x , this.fOffsetL ) : translationValue.x + ( tx - translationValue.x );

				}
				else {

					ftx = translationValue.x + ( tx - translationValue.x );

				}

				if( translationValue.y > 0 && this.fOffsetB + translationValue.y >= 0 ) {

					fty = ( this.fOffsetT >= 0 ) ? Math.min( translationValue.y , this.fOffsetB ) : translationValue.y + ( ty - translationValue.y );

				}
				else if( translationValue.y < 0 && this.fOffsetT + translationValue.y >= 0 ) {

					fty = ( this.fOffsetB >= 0 ) ? Math.min( translationValue.y , this.fOffsetT ) : translationValue.y + ( ty - translationValue.y );

				}
				else {

					fty = translationValue.y + ( ty - translationValue.y );

				}

			}

			return {
				ftx : ftx,
				fty : fty
			};

		},
		// sets the last step's content
		_setLastStep : function( direction, styleCSS ) {

			var contentBottom, contentTopBack,
				contentBottomStyle = '',
				contentTopBackStyle = '';

			switch( direction ) {

				case 'bottom' :
					contentTopBackStyle = 'margin-top: -' + styleCSS.height + 'px';
					break;
				case 'top' : 
					contentBottomStyle = 'margin-top: -' + styleCSS.height + 'px';
					break;
				case 'left' :
					contentTopBackStyle = 'width:' + ( styleCSS.width * 2 ) + 'px';
					contentBottomStyle = 'width:' + ( styleCSS.width * 2 ) + 'px;margin-left: -' + styleCSS.width + 'px';
					break;
				case 'right' :
					contentTopBackStyle = 'with:' + ( styleCSS.width * 2 ) + 'px;margin-left: -' + styleCSS.width + 'px';
					contentBottomStyle = 'width:' + ( styleCSS.width * 2 ) + 'px';
					break;

			}

			contentBottom = '<div class="uc-inner"><div class="uc-inner-content" style="' + contentBottomStyle + '">' + this.fContent + '</div></div>';

			var contentTopBackClasses = direction === 'top' || direction === 'bottom' ? 'uc-inner uc-inner-rotate' : 'uc-inner';
				contentTopBack = '<div class="' + contentTopBackClasses + '"><div class="uc-inner-content" style="' + contentTopBackStyle + '">' + this.fContent + '</div></div>';

			return {
				bottom : contentBottom,
				top : contentTopBack
			};

		},
		// adds overlays to the "(un)folding" elements if the options.overlays is true
		_addOverlays : function( action, $bottomEl, $topEl ) {

			var bottomOverlayStyle, topFrontOverlayStyle, topBackOverlayStyle;

			this.$bottomOverlay = $( '<div class="uc-overlay"></div>' );
			this.$topFrontOverlay = $( '<div class="uc-flipoverlay"></div>' );
			this.$topBackOverlay = $( '<div class="uc-flipoverlay"></div>' );

			if( action === 'fold' ) {

				bottomOverlayStyle = {
					transition : 'opacity ' + ( this.options.speed / 2 ) + 'ms ' + this.options.easing + ' ' + ( this.options.speed / 2 ) + 'ms'
				};

				topFrontOverlayStyle = {
					opacity : .5,
					transition : 'opacity ' + ( this.options.speed / 2 ) + 'ms ' + this.options.easing
				};

				topBackOverlayStyle = {
					opacity : 0,
					transition : 'opacity ' + ( this.options.speed / 2 ) + 'ms ' + this.options.easing
				};

			}
			else {

				bottomOverlayStyle = {
					opacity : 1,
					transition : 'opacity ' + ( this.options.speed / 2 ) + 'ms ' + this.options.easing
				};

				topFrontOverlayStyle = {
					transition : 'opacity ' + ( this.options.speed / 2 ) + 'ms ' + this.options.easing
				};

				topBackOverlayStyle = {
					opacity : .5,
					transition : 'opacity ' + ( this.options.speed / 2 ) + 'ms ' + this.options.easing + ' ' + ( this.options.speed / 2 ) + 'ms'
				};

			}

			$bottomEl.append( this.$bottomOverlay.css( bottomOverlayStyle ) );
			$topEl.children( 'div.uc-front' )
				  .append( this.$topFrontOverlay.css( topFrontOverlayStyle ) )
				  .end()
				  .children( 'div.uc-back' )
				  .append( this.$topBackOverlay.css( topBackOverlayStyle ) );

		},
		// public method: unfolds the element
		unfold : function() {

			// if opened already or currently (un)folding return
			if( this.opened || this.animating ) {

				return false;

			}

			this.animating = true;
			this._start( 'unfold' );

		},
		// public method: folds the element
		fold : function() {

			// if not opened or currently (un)folding return
			if( !this.opened || this.animating ) {

				return false;

			}

			this.animating = true;
			this._start( 'fold' );

		},
		// public method: returns 'opened' or 'closed'
		getStatus : function() {

			return ( this.opened ) ? 'opened' : 'closed';

		}

	};
	
	var logError = function( message ) {

		if ( window.console ) {

			window.console.error( message );
		
		}

	};
	
	$.fn.pfold = function( options ) {

		var instance = $.data( this, 'pfold' );
		
		if ( typeof options === 'string' ) {
			
			var args = Array.prototype.slice.call( arguments, 1 );
			
			this.each(function() {
			
				if ( !instance ) {

					logError( "cannot call methods on pfold prior to initialization; " +
					"attempted to call method '" + options + "'" );
					return;
				
				}
				
				if ( !$.isFunction( instance[options] ) || options.charAt(0) === "_" ) {

					logError( "no such method '" + options + "' for pfold instance" );
					return;
				
				}
				
				instance[ options ].apply( instance, args );
			
			});
		
		} 
		else {
		
			this.each(function() {
				
				if ( instance ) {

					instance._init();
				
				}
				else {

					instance = $.data( this, 'pfold', new $.PFold( options, this ) );
				
				}

			});
		
		}
		
		return instance;
		
	};
	
} )( jQuery, window );