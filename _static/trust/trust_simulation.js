(function (lib, img, cjs, ss, an) {

var p; // shortcut to reference prototypes
lib.webFontTxtInst = {}; 
var loadedTypekitCount = 0;
var loadedGoogleCount = 0;
var gFontsUpdateCacheList = [];
var tFontsUpdateCacheList = [];
lib.ssMetadata = [];



lib.updateListCache = function (cacheList) {		
	for(var i = 0; i < cacheList.length; i++) {		
		if(cacheList[i].cacheCanvas)		
			cacheList[i].updateCache();		
	}		
};		

lib.addElementsToCache = function (textInst, cacheList) {		
	var cur = textInst;		
	while(cur != exportRoot) {		
		if(cacheList.indexOf(cur) != -1)		
			break;		
		cur = cur.parent;		
	}		
	if(cur != exportRoot) {		
		var cur2 = textInst;		
		var index = cacheList.indexOf(cur);		
		while(cur2 != cur) {		
			cacheList.splice(index, 0, cur2);		
			cur2 = cur2.parent;		
			index++;		
		}		
	}		
	else {		
		cur = textInst;		
		while(cur != exportRoot) {		
			cacheList.push(cur);		
			cur = cur.parent;		
		}		
	}		
};		

lib.gfontAvailable = function(family, totalGoogleCount) {		
	lib.properties.webfonts[family] = true;		
	var txtInst = lib.webFontTxtInst && lib.webFontTxtInst[family] || [];		
	for(var f = 0; f < txtInst.length; ++f)		
		lib.addElementsToCache(txtInst[f], gFontsUpdateCacheList);		

	loadedGoogleCount++;		
	if(loadedGoogleCount == totalGoogleCount) {		
		lib.updateListCache(gFontsUpdateCacheList);		
	}		
};		

lib.tfontAvailable = function(family, totalTypekitCount) {		
	lib.properties.webfonts[family] = true;		
	var txtInst = lib.webFontTxtInst && lib.webFontTxtInst[family] || [];		
	for(var f = 0; f < txtInst.length; ++f)		
		lib.addElementsToCache(txtInst[f], tFontsUpdateCacheList);		

	loadedTypekitCount++;		
	if(loadedTypekitCount == totalTypekitCount) {		
		lib.updateListCache(tFontsUpdateCacheList);		
	}		
};
// symbols:
// helper functions:

function mc_symbol_clone() {
	var clone = this._cloneProps(new this.constructor(this.mode, this.startPosition, this.loop));
	clone.gotoAndStop(this.currentFrame);
	clone.paused = this.paused;
	clone.framerate = this.framerate;
	return clone;
}

function getMCSymbolPrototype(symbol, nominalBounds, frameBounds) {
	var prototype = cjs.extend(symbol, cjs.MovieClip);
	prototype.clone = mc_symbol_clone;
	prototype.nominalBounds = nominalBounds;
	prototype.frameBounds = frameBounds;
	return prototype;
	}


(lib.participantLabel = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.label = new cjs.Text("participant A", "bold 20px 'Gotham Bold'");
	this.label.name = "label";
	this.label.lineHeight = 20;
	this.label.lineWidth = 160;
	this.label.parent = this;
	this.label.setTransform(22.2,7.4,0.714,0.847,0,-0.3,32.2);

	this.timeline.addTween(cjs.Tween.get(this.label).wait(1));

}).prototype = getMCSymbolPrototype(lib.participantLabel, new cjs.Rectangle(21,5,99.2,97.6), null);


(lib.multiplier = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.label = new cjs.Text("×3", "bold 40px 'Gotham Bold'");
	this.label.name = "label";
	this.label.textAlign = "center";
	this.label.lineHeight = 49;
	this.label.lineWidth = 100;
	this.label.parent = this;
	this.label.setTransform(-4.4,-8.9);

	this.timeline.addTween(cjs.Tween.get(this.label).wait(1));

	// Calque 2
	this.shape = new cjs.Shape();
	this.shape.graphics.f().s("#000000").ss(6,1,0,3).p("AJKAAQAADzisCrQirCsjzAAQjyAAirisQisirAAjzQAAjyCsirQCrisDyAAQDzAACrCsQCsCrAADyg");

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("rgba(160,160,160,0.698)").s().p("AmdGeQisisAAjyQAAjxCsisQCsisDxAAQDyAACsCsQCsCsAADxQAADyisCsQisCsjyAAQjxAAisisg");

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = getMCSymbolPrototype(lib.multiplier, new cjs.Rectangle(-61.5,-61.5,123.1,123.1), null);


(lib.floor = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// mask (mask)
	var mask = new cjs.Shape();
	mask._off = true;
	mask.graphics.p("Egu3AlgMAAAhK/MBdvAAAMAAABK/g");
	mask.setTransform(24.9,39.9);

	// grid
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape.setTransform(-1183.9,39.9,1.188,1.188);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_1.setTransform(-1160.2,39.9,1.188,1.188);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_2.setTransform(-1136.4,39.9,1.188,1.188);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_3.setTransform(-1112.6,39.9,1.188,1.188);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_4.setTransform(-1088.9,39.9,1.188,1.188);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_5.setTransform(-1065.1,39.9,1.188,1.188);

	this.shape_6 = new cjs.Shape();
	this.shape_6.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_6.setTransform(-1041.3,39.9,1.188,1.188);

	this.shape_7 = new cjs.Shape();
	this.shape_7.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_7.setTransform(-1017.6,39.9,1.188,1.188);

	this.shape_8 = new cjs.Shape();
	this.shape_8.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_8.setTransform(-993.8,39.9,1.188,1.188);

	this.shape_9 = new cjs.Shape();
	this.shape_9.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_9.setTransform(-970,39.9,1.188,1.188);

	this.shape_10 = new cjs.Shape();
	this.shape_10.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_10.setTransform(-946.3,39.9,1.188,1.188);

	this.shape_11 = new cjs.Shape();
	this.shape_11.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_11.setTransform(-922.5,39.9,1.188,1.188);

	this.shape_12 = new cjs.Shape();
	this.shape_12.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_12.setTransform(-898.7,39.9,1.188,1.188);

	this.shape_13 = new cjs.Shape();
	this.shape_13.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_13.setTransform(-875,39.9,1.188,1.188);

	this.shape_14 = new cjs.Shape();
	this.shape_14.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_14.setTransform(-851.2,39.9,1.188,1.188);

	this.shape_15 = new cjs.Shape();
	this.shape_15.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_15.setTransform(-827.4,39.9,1.188,1.188);

	this.shape_16 = new cjs.Shape();
	this.shape_16.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_16.setTransform(-803.7,39.9,1.188,1.188);

	this.shape_17 = new cjs.Shape();
	this.shape_17.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUaBCLg");
	this.shape_17.setTransform(-779.9,39.9,1.188,1.188);

	this.shape_18 = new cjs.Shape();
	this.shape_18.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUZBCLg");
	this.shape_18.setTransform(-756.2,39.9,1.188,1.188);

	this.shape_19 = new cjs.Shape();
	this.shape_19.graphics.f("#000000").s().p("EhKMAhFMCUZhCLIAAACMiUYBCLg");
	this.shape_19.setTransform(-732.4,39.9,1.188,1.188);

	this.shape_20 = new cjs.Shape();
	this.shape_20.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUZBCLg");
	this.shape_20.setTransform(-708.6,39.9,1.188,1.188);

	this.shape_21 = new cjs.Shape();
	this.shape_21.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUZBCLg");
	this.shape_21.setTransform(-684.9,39.9,1.188,1.188);

	this.shape_22 = new cjs.Shape();
	this.shape_22.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUaBCLg");
	this.shape_22.setTransform(-661.1,39.9,1.188,1.188);

	this.shape_23 = new cjs.Shape();
	this.shape_23.graphics.f("#000000").s().p("EhKMAhFMCUZhCLIAAACMiUYBCLg");
	this.shape_23.setTransform(-637.3,39.9,1.188,1.188);

	this.shape_24 = new cjs.Shape();
	this.shape_24.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_24.setTransform(-613.6,39.9,1.188,1.188);

	this.shape_25 = new cjs.Shape();
	this.shape_25.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUZBCLg");
	this.shape_25.setTransform(-589.8,39.9,1.188,1.188);

	this.shape_26 = new cjs.Shape();
	this.shape_26.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUaBCLg");
	this.shape_26.setTransform(-566,39.9,1.188,1.188);

	this.shape_27 = new cjs.Shape();
	this.shape_27.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUZBCLg");
	this.shape_27.setTransform(-542.3,39.9,1.188,1.188);

	this.shape_28 = new cjs.Shape();
	this.shape_28.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_28.setTransform(-518.5,39.9,1.188,1.188);

	this.shape_29 = new cjs.Shape();
	this.shape_29.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUZBCLg");
	this.shape_29.setTransform(-494.7,39.9,1.188,1.188);

	this.shape_30 = new cjs.Shape();
	this.shape_30.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUZBCLg");
	this.shape_30.setTransform(-471,39.9,1.188,1.188);

	this.shape_31 = new cjs.Shape();
	this.shape_31.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUaBCLg");
	this.shape_31.setTransform(-447.2,39.9,1.188,1.188);

	this.shape_32 = new cjs.Shape();
	this.shape_32.graphics.f("#000000").s().p("EhKMAhFMCUZhCLIAAACMiUYBCLg");
	this.shape_32.setTransform(-423.4,39.9,1.188,1.188);

	this.shape_33 = new cjs.Shape();
	this.shape_33.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_33.setTransform(-399.7,39.9,1.188,1.188);

	this.shape_34 = new cjs.Shape();
	this.shape_34.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUZBCLg");
	this.shape_34.setTransform(-375.9,39.9,1.188,1.188);

	this.shape_35 = new cjs.Shape();
	this.shape_35.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUaBCLg");
	this.shape_35.setTransform(-352.1,39.9,1.188,1.188);

	this.shape_36 = new cjs.Shape();
	this.shape_36.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUZBCLg");
	this.shape_36.setTransform(-328.4,39.9,1.188,1.188);

	this.shape_37 = new cjs.Shape();
	this.shape_37.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_37.setTransform(-304.6,39.9,1.188,1.188);

	this.shape_38 = new cjs.Shape();
	this.shape_38.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUZBCLg");
	this.shape_38.setTransform(-280.8,39.9,1.188,1.188);

	this.shape_39 = new cjs.Shape();
	this.shape_39.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUZBCLg");
	this.shape_39.setTransform(-257.1,39.9,1.188,1.188);

	this.shape_40 = new cjs.Shape();
	this.shape_40.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUaBCLg");
	this.shape_40.setTransform(-233.3,39.9,1.188,1.188);

	this.shape_41 = new cjs.Shape();
	this.shape_41.graphics.f("#000000").s().p("EhKMAhFMCUZhCLIAAACMiUYBCLg");
	this.shape_41.setTransform(-209.5,39.9,1.188,1.188);

	this.shape_42 = new cjs.Shape();
	this.shape_42.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_42.setTransform(-185.8,39.9,1.188,1.188);

	this.shape_43 = new cjs.Shape();
	this.shape_43.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUZBCLg");
	this.shape_43.setTransform(-162,39.9,1.188,1.188);

	this.shape_44 = new cjs.Shape();
	this.shape_44.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUaBCLg");
	this.shape_44.setTransform(-138.2,39.9,1.188,1.188);

	this.shape_45 = new cjs.Shape();
	this.shape_45.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUZBCLg");
	this.shape_45.setTransform(-114.5,39.9,1.188,1.188);

	this.shape_46 = new cjs.Shape();
	this.shape_46.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_46.setTransform(-90.7,39.9,1.188,1.188);

	this.shape_47 = new cjs.Shape();
	this.shape_47.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUZBCLg");
	this.shape_47.setTransform(-66.9,39.9,1.188,1.188);

	this.shape_48 = new cjs.Shape();
	this.shape_48.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUZBCLg");
	this.shape_48.setTransform(-43.2,39.9,1.188,1.188);

	this.shape_49 = new cjs.Shape();
	this.shape_49.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUaBCLg");
	this.shape_49.setTransform(-19.4,39.9,1.188,1.188);

	this.shape_50 = new cjs.Shape();
	this.shape_50.graphics.f("#000000").s().p("EhKMAhFMCUZhCLIAAACMiUYBCLg");
	this.shape_50.setTransform(4.4,39.9,1.188,1.188);

	this.shape_51 = new cjs.Shape();
	this.shape_51.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_51.setTransform(28.1,39.9,1.188,1.188);

	this.shape_52 = new cjs.Shape();
	this.shape_52.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUZBCLg");
	this.shape_52.setTransform(51.9,39.9,1.188,1.188);

	this.shape_53 = new cjs.Shape();
	this.shape_53.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUaBCLg");
	this.shape_53.setTransform(75.7,39.9,1.188,1.188);

	this.shape_54 = new cjs.Shape();
	this.shape_54.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_54.setTransform(-1018,43.1,1.188,1.188);

	this.shape_55 = new cjs.Shape();
	this.shape_55.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_55.setTransform(-994.2,43.1,1.188,1.188);

	this.shape_56 = new cjs.Shape();
	this.shape_56.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_56.setTransform(-970.5,43.1,1.188,1.188);

	this.shape_57 = new cjs.Shape();
	this.shape_57.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_57.setTransform(-946.7,43.1,1.188,1.188);

	this.shape_58 = new cjs.Shape();
	this.shape_58.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_58.setTransform(-923,43.1,1.188,1.188);

	this.shape_59 = new cjs.Shape();
	this.shape_59.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_59.setTransform(-899.2,43.1,1.188,1.188);

	this.shape_60 = new cjs.Shape();
	this.shape_60.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_60.setTransform(-875.4,43.1,1.188,1.188);

	this.shape_61 = new cjs.Shape();
	this.shape_61.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgCACg");
	this.shape_61.setTransform(-851.7,43.1,1.188,1.188);

	this.shape_62 = new cjs.Shape();
	this.shape_62.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_62.setTransform(-827.9,43.1,1.188,1.188);

	this.shape_63 = new cjs.Shape();
	this.shape_63.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_63.setTransform(-804.1,43.1,1.188,1.188);

	this.shape_64 = new cjs.Shape();
	this.shape_64.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_64.setTransform(-780.4,43.1,1.188,1.188);

	this.shape_65 = new cjs.Shape();
	this.shape_65.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_65.setTransform(-756.6,43.1,1.188,1.188);

	this.shape_66 = new cjs.Shape();
	this.shape_66.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_66.setTransform(-732.8,43.1,1.188,1.188);

	this.shape_67 = new cjs.Shape();
	this.shape_67.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_67.setTransform(-709.1,43.1,1.188,1.188);

	this.shape_68 = new cjs.Shape();
	this.shape_68.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_68.setTransform(-685.3,43.1,1.188,1.188);

	this.shape_69 = new cjs.Shape();
	this.shape_69.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_69.setTransform(-661.5,43.1,1.188,1.188);

	this.shape_70 = new cjs.Shape();
	this.shape_70.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgCACg");
	this.shape_70.setTransform(-637.8,43.1,1.188,1.188);

	this.shape_71 = new cjs.Shape();
	this.shape_71.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_71.setTransform(-614,43.1,1.188,1.188);

	this.shape_72 = new cjs.Shape();
	this.shape_72.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIAAACg");
	this.shape_72.setTransform(-590.2,43.1,1.188,1.188);

	this.shape_73 = new cjs.Shape();
	this.shape_73.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_73.setTransform(-566.5,43.1,1.188,1.188);

	this.shape_74 = new cjs.Shape();
	this.shape_74.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_74.setTransform(-542.7,43.1,1.188,1.188);

	this.shape_75 = new cjs.Shape();
	this.shape_75.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgCACg");
	this.shape_75.setTransform(-518.9,43.1,1.188,1.188);

	this.shape_76 = new cjs.Shape();
	this.shape_76.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_76.setTransform(-495.2,43.1,1.188,1.188);

	this.shape_77 = new cjs.Shape();
	this.shape_77.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_77.setTransform(-471.4,43.1,1.188,1.188);

	this.shape_78 = new cjs.Shape();
	this.shape_78.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_78.setTransform(-447.6,43.1,1.188,1.188);

	this.shape_79 = new cjs.Shape();
	this.shape_79.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIgBACg");
	this.shape_79.setTransform(-423.9,43.1,1.188,1.188);

	this.shape_80 = new cjs.Shape();
	this.shape_80.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_80.setTransform(-400.1,43.1,1.188,1.188);

	this.shape_81 = new cjs.Shape();
	this.shape_81.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIAAACg");
	this.shape_81.setTransform(-376.3,43.1,1.188,1.188);

	this.shape_82 = new cjs.Shape();
	this.shape_82.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_82.setTransform(-352.6,43.1,1.188,1.188);

	this.shape_83 = new cjs.Shape();
	this.shape_83.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_83.setTransform(-328.8,43.1,1.188,1.188);

	this.shape_84 = new cjs.Shape();
	this.shape_84.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgCACg");
	this.shape_84.setTransform(-305,43.1,1.188,1.188);

	this.shape_85 = new cjs.Shape();
	this.shape_85.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_85.setTransform(-281.3,43.1,1.188,1.188);

	this.shape_86 = new cjs.Shape();
	this.shape_86.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_86.setTransform(-257.5,43.1,1.188,1.188);

	this.shape_87 = new cjs.Shape();
	this.shape_87.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_87.setTransform(-233.7,43.1,1.188,1.188);

	this.shape_88 = new cjs.Shape();
	this.shape_88.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_88.setTransform(-210,43.1,1.188,1.188);

	this.shape_89 = new cjs.Shape();
	this.shape_89.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_89.setTransform(-186.2,43.1,1.188,1.188);

	this.shape_90 = new cjs.Shape();
	this.shape_90.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIAAACg");
	this.shape_90.setTransform(-162.4,43.1,1.188,1.188);

	this.shape_91 = new cjs.Shape();
	this.shape_91.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_91.setTransform(-138.7,43.1,1.188,1.188);

	this.shape_92 = new cjs.Shape();
	this.shape_92.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_92.setTransform(-114.9,43.1,1.188,1.188);

	this.shape_93 = new cjs.Shape();
	this.shape_93.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgCACg");
	this.shape_93.setTransform(-91.1,43.1,1.188,1.188);

	this.shape_94 = new cjs.Shape();
	this.shape_94.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUZBCLg");
	this.shape_94.setTransform(99.4,39.9,1.188,1.188);

	this.shape_95 = new cjs.Shape();
	this.shape_95.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_95.setTransform(123.2,39.9,1.188,1.188);

	this.shape_96 = new cjs.Shape();
	this.shape_96.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUZBCLg");
	this.shape_96.setTransform(147,39.9,1.188,1.188);

	this.shape_97 = new cjs.Shape();
	this.shape_97.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIACACMiUaBCLg");
	this.shape_97.setTransform(170.7,39.9,1.188,1.188);

	this.shape_98 = new cjs.Shape();
	this.shape_98.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUaBCLg");
	this.shape_98.setTransform(194.5,39.9,1.188,1.188);

	this.shape_99 = new cjs.Shape();
	this.shape_99.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUYBCLg");
	this.shape_99.setTransform(218.3,39.9,1.188,1.188);

	this.shape_100 = new cjs.Shape();
	this.shape_100.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_100.setTransform(242,39.9,1.188,1.188);

	this.shape_101 = new cjs.Shape();
	this.shape_101.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUZBCLg");
	this.shape_101.setTransform(265.8,39.9,1.188,1.188);

	this.shape_102 = new cjs.Shape();
	this.shape_102.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIACACMiUaBCLg");
	this.shape_102.setTransform(289.6,39.9,1.188,1.188);

	this.shape_103 = new cjs.Shape();
	this.shape_103.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUZBCLg");
	this.shape_103.setTransform(313.3,39.9,1.188,1.188);

	this.shape_104 = new cjs.Shape();
	this.shape_104.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_104.setTransform(337.1,39.9,1.188,1.188);

	this.shape_105 = new cjs.Shape();
	this.shape_105.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUZBCLg");
	this.shape_105.setTransform(360.9,39.9,1.188,1.188);

	this.shape_106 = new cjs.Shape();
	this.shape_106.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIACACMiUaBCLg");
	this.shape_106.setTransform(384.7,39.9,1.188,1.188);

	this.shape_107 = new cjs.Shape();
	this.shape_107.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUaBCLg");
	this.shape_107.setTransform(408.4,39.9,1.188,1.188);

	this.shape_108 = new cjs.Shape();
	this.shape_108.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUYBCLg");
	this.shape_108.setTransform(432.2,39.9,1.188,1.188);

	this.shape_109 = new cjs.Shape();
	this.shape_109.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_109.setTransform(456,39.9,1.188,1.188);

	this.shape_110 = new cjs.Shape();
	this.shape_110.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUZBCLg");
	this.shape_110.setTransform(479.7,39.9,1.188,1.188);

	this.shape_111 = new cjs.Shape();
	this.shape_111.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIACACMiUaBCLg");
	this.shape_111.setTransform(503.5,39.9,1.188,1.188);

	this.shape_112 = new cjs.Shape();
	this.shape_112.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUZBCLg");
	this.shape_112.setTransform(527.3,39.9,1.188,1.188);

	this.shape_113 = new cjs.Shape();
	this.shape_113.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_113.setTransform(551,39.9,1.188,1.188);

	this.shape_114 = new cjs.Shape();
	this.shape_114.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUZBCLg");
	this.shape_114.setTransform(574.8,39.9,1.188,1.188);

	this.shape_115 = new cjs.Shape();
	this.shape_115.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIACACMiUaBCLg");
	this.shape_115.setTransform(598.6,39.9,1.188,1.188);

	this.shape_116 = new cjs.Shape();
	this.shape_116.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUaBCLg");
	this.shape_116.setTransform(622.3,39.9,1.188,1.188);

	this.shape_117 = new cjs.Shape();
	this.shape_117.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUYBCLg");
	this.shape_117.setTransform(646.1,39.9,1.188,1.188);

	this.shape_118 = new cjs.Shape();
	this.shape_118.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_118.setTransform(669.9,39.9,1.188,1.188);

	this.shape_119 = new cjs.Shape();
	this.shape_119.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUZBCLg");
	this.shape_119.setTransform(693.6,39.9,1.188,1.188);

	this.shape_120 = new cjs.Shape();
	this.shape_120.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIACACMiUaBCLg");
	this.shape_120.setTransform(717.4,39.9,1.188,1.188);

	this.shape_121 = new cjs.Shape();
	this.shape_121.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUZBCLg");
	this.shape_121.setTransform(741.2,39.9,1.188,1.188);

	this.shape_122 = new cjs.Shape();
	this.shape_122.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_122.setTransform(764.9,39.9,1.188,1.188);

	this.shape_123 = new cjs.Shape();
	this.shape_123.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUZBCLg");
	this.shape_123.setTransform(788.7,39.9,1.188,1.188);

	this.shape_124 = new cjs.Shape();
	this.shape_124.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIACACMiUaBCLg");
	this.shape_124.setTransform(812.5,39.9,1.188,1.188);

	this.shape_125 = new cjs.Shape();
	this.shape_125.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUaBCLg");
	this.shape_125.setTransform(836.2,39.9,1.188,1.188);

	this.shape_126 = new cjs.Shape();
	this.shape_126.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUYBCLg");
	this.shape_126.setTransform(860,39.9,1.188,1.188);

	this.shape_127 = new cjs.Shape();
	this.shape_127.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_127.setTransform(883.8,39.9,1.188,1.188);

	this.shape_128 = new cjs.Shape();
	this.shape_128.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUZBCLg");
	this.shape_128.setTransform(907.5,39.9,1.188,1.188);

	this.shape_129 = new cjs.Shape();
	this.shape_129.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIACACMiUaBCLg");
	this.shape_129.setTransform(931.3,39.9,1.188,1.188);

	this.shape_130 = new cjs.Shape();
	this.shape_130.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUZBCLg");
	this.shape_130.setTransform(955.1,39.9,1.188,1.188);

	this.shape_131 = new cjs.Shape();
	this.shape_131.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_131.setTransform(978.8,39.9,1.188,1.188);

	this.shape_132 = new cjs.Shape();
	this.shape_132.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUZBCLg");
	this.shape_132.setTransform(1002.6,39.9,1.188,1.188);

	this.shape_133 = new cjs.Shape();
	this.shape_133.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIACACMiUaBCLg");
	this.shape_133.setTransform(1026.4,39.9,1.188,1.188);

	this.shape_134 = new cjs.Shape();
	this.shape_134.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUaBCLg");
	this.shape_134.setTransform(1050.1,39.9,1.188,1.188);

	this.shape_135 = new cjs.Shape();
	this.shape_135.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUYBCLg");
	this.shape_135.setTransform(1073.9,39.9,1.188,1.188);

	this.shape_136 = new cjs.Shape();
	this.shape_136.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_136.setTransform(1097.7,39.9,1.188,1.188);

	this.shape_137 = new cjs.Shape();
	this.shape_137.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIABACMiUZBCLg");
	this.shape_137.setTransform(1121.4,39.9,1.188,1.188);

	this.shape_138 = new cjs.Shape();
	this.shape_138.graphics.f("#000000").s().p("EhKNAhFMCUZhCLIACACMiUaBCLg");
	this.shape_138.setTransform(1145.2,39.9,1.188,1.188);

	this.shape_139 = new cjs.Shape();
	this.shape_139.graphics.f("#000000").s().p("EhKNAhFMCUahCLIABACMiUZBCLg");
	this.shape_139.setTransform(1169,39.9,1.188,1.188);

	this.shape_140 = new cjs.Shape();
	this.shape_140.graphics.f("#000000").s().p("EhKMAhFMCUYhCLIABACMiUYBCLg");
	this.shape_140.setTransform(1192.7,39.9,1.188,1.188);

	this.shape_141 = new cjs.Shape();
	this.shape_141.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_141.setTransform(-67.4,43.1,1.188,1.188);

	this.shape_142 = new cjs.Shape();
	this.shape_142.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_142.setTransform(-43.6,43.1,1.188,1.188);

	this.shape_143 = new cjs.Shape();
	this.shape_143.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_143.setTransform(-19.8,43.1,1.188,1.188);

	this.shape_144 = new cjs.Shape();
	this.shape_144.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_144.setTransform(3.9,43.1,1.188,1.188);

	this.shape_145 = new cjs.Shape();
	this.shape_145.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_145.setTransform(27.7,43.1,1.188,1.188);

	this.shape_146 = new cjs.Shape();
	this.shape_146.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIAAACg");
	this.shape_146.setTransform(51.5,43.1,1.188,1.188);

	this.shape_147 = new cjs.Shape();
	this.shape_147.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_147.setTransform(75.2,43.1,1.188,1.188);

	this.shape_148 = new cjs.Shape();
	this.shape_148.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_148.setTransform(99,43.1,1.188,1.188);

	this.shape_149 = new cjs.Shape();
	this.shape_149.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgCACg");
	this.shape_149.setTransform(122.8,43.1,1.188,1.188);

	this.shape_150 = new cjs.Shape();
	this.shape_150.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_150.setTransform(146.5,43.1,1.188,1.188);

	this.shape_151 = new cjs.Shape();
	this.shape_151.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_151.setTransform(170.3,43.1,1.188,1.188);

	this.shape_152 = new cjs.Shape();
	this.shape_152.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_152.setTransform(194.1,43.1,1.188,1.188);

	this.shape_153 = new cjs.Shape();
	this.shape_153.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIgBACg");
	this.shape_153.setTransform(217.8,43.1,1.188,1.188);

	this.shape_154 = new cjs.Shape();
	this.shape_154.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_154.setTransform(241.6,43.1,1.188,1.188);

	this.shape_155 = new cjs.Shape();
	this.shape_155.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIAAACg");
	this.shape_155.setTransform(265.4,43.1,1.188,1.188);

	this.shape_156 = new cjs.Shape();
	this.shape_156.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_156.setTransform(289.1,43.1,1.188,1.188);

	this.shape_157 = new cjs.Shape();
	this.shape_157.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_157.setTransform(312.9,43.1,1.188,1.188);

	this.shape_158 = new cjs.Shape();
	this.shape_158.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgCACg");
	this.shape_158.setTransform(336.7,43.1,1.188,1.188);

	this.shape_159 = new cjs.Shape();
	this.shape_159.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_159.setTransform(360.4,43.1,1.188,1.188);

	this.shape_160 = new cjs.Shape();
	this.shape_160.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIgBACg");
	this.shape_160.setTransform(384.2,43.1,1.188,1.188);

	this.shape_161 = new cjs.Shape();
	this.shape_161.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_161.setTransform(408,43.1,1.188,1.188);

	this.shape_162 = new cjs.Shape();
	this.shape_162.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIgBACg");
	this.shape_162.setTransform(431.7,43.1,1.188,1.188);

	this.shape_163 = new cjs.Shape();
	this.shape_163.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_163.setTransform(455.5,43.1,1.188,1.188);

	this.shape_164 = new cjs.Shape();
	this.shape_164.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIAAACg");
	this.shape_164.setTransform(479.3,43.1,1.188,1.188);

	this.shape_165 = new cjs.Shape();
	this.shape_165.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_165.setTransform(503,43.1,1.188,1.188);

	this.shape_166 = new cjs.Shape();
	this.shape_166.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_166.setTransform(526.8,43.1,1.188,1.188);

	this.shape_167 = new cjs.Shape();
	this.shape_167.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgCACg");
	this.shape_167.setTransform(550.6,43.1,1.188,1.188);

	this.shape_168 = new cjs.Shape();
	this.shape_168.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_168.setTransform(574.3,43.1,1.188,1.188);

	this.shape_169 = new cjs.Shape();
	this.shape_169.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIgBACg");
	this.shape_169.setTransform(598.1,43.1,1.188,1.188);

	this.shape_170 = new cjs.Shape();
	this.shape_170.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_170.setTransform(621.9,43.1,1.188,1.188);

	this.shape_171 = new cjs.Shape();
	this.shape_171.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIgBACg");
	this.shape_171.setTransform(645.6,43.1,1.188,1.188);

	this.shape_172 = new cjs.Shape();
	this.shape_172.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_172.setTransform(669.4,43.1,1.188,1.188);

	this.shape_173 = new cjs.Shape();
	this.shape_173.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIAAACg");
	this.shape_173.setTransform(693.2,43.1,1.188,1.188);

	this.shape_174 = new cjs.Shape();
	this.shape_174.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_174.setTransform(716.9,43.1,1.188,1.188);

	this.shape_175 = new cjs.Shape();
	this.shape_175.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_175.setTransform(740.7,43.1,1.188,1.188);

	this.shape_176 = new cjs.Shape();
	this.shape_176.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_176.setTransform(764.5,43.1,1.188,1.188);

	this.shape_177 = new cjs.Shape();
	this.shape_177.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIAAACg");
	this.shape_177.setTransform(788.2,43.1,1.188,1.188);

	this.shape_178 = new cjs.Shape();
	this.shape_178.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIgBACg");
	this.shape_178.setTransform(812,43.1,1.188,1.188);

	this.shape_179 = new cjs.Shape();
	this.shape_179.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_179.setTransform(835.8,43.1,1.188,1.188);

	this.shape_180 = new cjs.Shape();
	this.shape_180.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIgBACg");
	this.shape_180.setTransform(859.5,43.1,1.188,1.188);

	this.shape_181 = new cjs.Shape();
	this.shape_181.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_181.setTransform(883.3,43.1,1.188,1.188);

	this.shape_182 = new cjs.Shape();
	this.shape_182.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIAAACg");
	this.shape_182.setTransform(907.1,43.1,1.188,1.188);

	this.shape_183 = new cjs.Shape();
	this.shape_183.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_183.setTransform(930.8,43.1,1.188,1.188);

	this.shape_184 = new cjs.Shape();
	this.shape_184.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_184.setTransform(954.6,43.1,1.188,1.188);

	this.shape_185 = new cjs.Shape();
	this.shape_185.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_185.setTransform(978.4,43.1,1.188,1.188);

	this.shape_186 = new cjs.Shape();
	this.shape_186.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIAAACg");
	this.shape_186.setTransform(1002.1,43.1,1.188,1.188);

	this.shape_187 = new cjs.Shape();
	this.shape_187.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIgBACg");
	this.shape_187.setTransform(1025.9,43.1,1.188,1.188);

	this.shape_188 = new cjs.Shape();
	this.shape_188.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_188.setTransform(1049.7,43.1,1.188,1.188);

	this.shape_189 = new cjs.Shape();
	this.shape_189.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIgBACg");
	this.shape_189.setTransform(1073.4,43.1,1.188,1.188);

	this.shape_190 = new cjs.Shape();
	this.shape_190.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_190.setTransform(1097.2,43.1,1.188,1.188);

	this.shape_191 = new cjs.Shape();
	this.shape_191.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIAAACg");
	this.shape_191.setTransform(1121,43.1,1.188,1.188);

	this.shape_192 = new cjs.Shape();
	this.shape_192.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_192.setTransform(1144.7,43.1,1.188,1.188);

	this.shape_193 = new cjs.Shape();
	this.shape_193.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_193.setTransform(1168.5,43.1,1.188,1.188);

	this.shape_194 = new cjs.Shape();
	this.shape_194.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_194.setTransform(1192.3,43.1,1.188,1.188);

	this.shape_195 = new cjs.Shape();
	this.shape_195.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIAAACg");
	this.shape_195.setTransform(1216,43.1,1.188,1.188);

	this.shape_196 = new cjs.Shape();
	this.shape_196.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIgBACg");
	this.shape_196.setTransform(1239.8,43.1,1.188,1.188);

	this.shape_197 = new cjs.Shape();
	this.shape_197.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_197.setTransform(1263.6,43.1,1.188,1.188);

	this.shape_198 = new cjs.Shape();
	this.shape_198.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIgBACg");
	this.shape_198.setTransform(1287.3,43.1,1.188,1.188);

	this.shape_199 = new cjs.Shape();
	this.shape_199.graphics.f("#000000").s().p("Eg0EggpIACgDMBoHBBXIgBACg");
	this.shape_199.setTransform(1311.1,43.1,1.188,1.188);

	this.shape_200 = new cjs.Shape();
	this.shape_200.graphics.f("#000000").s().p("Eg0EggpIACgDMBoGBBXIAAACg");
	this.shape_200.setTransform(1334.9,43.1,1.188,1.188);

	this.shape_201 = new cjs.Shape();
	this.shape_201.graphics.f("#000000").s().p("Eg0DggpIABgDMBoGBBXIgBACg");
	this.shape_201.setTransform(1358.6,43.1,1.188,1.188);

	var maskedShapeInstanceList = [this.shape,this.shape_1,this.shape_2,this.shape_3,this.shape_4,this.shape_5,this.shape_6,this.shape_7,this.shape_8,this.shape_9,this.shape_10,this.shape_11,this.shape_12,this.shape_13,this.shape_14,this.shape_15,this.shape_16,this.shape_17,this.shape_18,this.shape_19,this.shape_20,this.shape_21,this.shape_22,this.shape_23,this.shape_24,this.shape_25,this.shape_26,this.shape_27,this.shape_28,this.shape_29,this.shape_30,this.shape_31,this.shape_32,this.shape_33,this.shape_34,this.shape_35,this.shape_36,this.shape_37,this.shape_38,this.shape_39,this.shape_40,this.shape_41,this.shape_42,this.shape_43,this.shape_44,this.shape_45,this.shape_46,this.shape_47,this.shape_48,this.shape_49,this.shape_50,this.shape_51,this.shape_52,this.shape_53,this.shape_54,this.shape_55,this.shape_56,this.shape_57,this.shape_58,this.shape_59,this.shape_60,this.shape_61,this.shape_62,this.shape_63,this.shape_64,this.shape_65,this.shape_66,this.shape_67,this.shape_68,this.shape_69,this.shape_70,this.shape_71,this.shape_72,this.shape_73,this.shape_74,this.shape_75,this.shape_76,this.shape_77,this.shape_78,this.shape_79,this.shape_80,this.shape_81,this.shape_82,this.shape_83,this.shape_84,this.shape_85,this.shape_86,this.shape_87,this.shape_88,this.shape_89,this.shape_90,this.shape_91,this.shape_92,this.shape_93,this.shape_94,this.shape_95,this.shape_96,this.shape_97,this.shape_98,this.shape_99,this.shape_100,this.shape_101,this.shape_102,this.shape_103,this.shape_104,this.shape_105,this.shape_106,this.shape_107,this.shape_108,this.shape_109,this.shape_110,this.shape_111,this.shape_112,this.shape_113,this.shape_114,this.shape_115,this.shape_116,this.shape_117,this.shape_118,this.shape_119,this.shape_120,this.shape_121,this.shape_122,this.shape_123,this.shape_124,this.shape_125,this.shape_126,this.shape_127,this.shape_128,this.shape_129,this.shape_130,this.shape_131,this.shape_132,this.shape_133,this.shape_134,this.shape_135,this.shape_136,this.shape_137,this.shape_138,this.shape_139,this.shape_140,this.shape_141,this.shape_142,this.shape_143,this.shape_144,this.shape_145,this.shape_146,this.shape_147,this.shape_148,this.shape_149,this.shape_150,this.shape_151,this.shape_152,this.shape_153,this.shape_154,this.shape_155,this.shape_156,this.shape_157,this.shape_158,this.shape_159,this.shape_160,this.shape_161,this.shape_162,this.shape_163,this.shape_164,this.shape_165,this.shape_166,this.shape_167,this.shape_168,this.shape_169,this.shape_170,this.shape_171,this.shape_172,this.shape_173,this.shape_174,this.shape_175,this.shape_176,this.shape_177,this.shape_178,this.shape_179,this.shape_180,this.shape_181,this.shape_182,this.shape_183,this.shape_184,this.shape_185,this.shape_186,this.shape_187,this.shape_188,this.shape_189,this.shape_190,this.shape_191,this.shape_192,this.shape_193,this.shape_194,this.shape_195,this.shape_196,this.shape_197,this.shape_198,this.shape_199,this.shape_200,this.shape_201];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_201},{t:this.shape_200},{t:this.shape_199},{t:this.shape_198},{t:this.shape_197},{t:this.shape_196},{t:this.shape_195},{t:this.shape_194},{t:this.shape_193},{t:this.shape_192},{t:this.shape_191},{t:this.shape_190},{t:this.shape_189},{t:this.shape_188},{t:this.shape_187},{t:this.shape_186},{t:this.shape_185},{t:this.shape_184},{t:this.shape_183},{t:this.shape_182},{t:this.shape_181},{t:this.shape_180},{t:this.shape_179},{t:this.shape_178},{t:this.shape_177},{t:this.shape_176},{t:this.shape_175},{t:this.shape_174},{t:this.shape_173},{t:this.shape_172},{t:this.shape_171},{t:this.shape_170},{t:this.shape_169},{t:this.shape_168},{t:this.shape_167},{t:this.shape_166},{t:this.shape_165},{t:this.shape_164},{t:this.shape_163},{t:this.shape_162},{t:this.shape_161},{t:this.shape_160},{t:this.shape_159},{t:this.shape_158},{t:this.shape_157},{t:this.shape_156},{t:this.shape_155},{t:this.shape_154},{t:this.shape_153},{t:this.shape_152},{t:this.shape_151},{t:this.shape_150},{t:this.shape_149},{t:this.shape_148},{t:this.shape_147},{t:this.shape_146},{t:this.shape_145},{t:this.shape_144},{t:this.shape_143},{t:this.shape_142},{t:this.shape_141},{t:this.shape_140},{t:this.shape_139},{t:this.shape_138},{t:this.shape_137},{t:this.shape_136},{t:this.shape_135},{t:this.shape_134},{t:this.shape_133},{t:this.shape_132},{t:this.shape_131},{t:this.shape_130},{t:this.shape_129},{t:this.shape_128},{t:this.shape_127},{t:this.shape_126},{t:this.shape_125},{t:this.shape_124},{t:this.shape_123},{t:this.shape_122},{t:this.shape_121},{t:this.shape_120},{t:this.shape_119},{t:this.shape_118},{t:this.shape_117},{t:this.shape_116},{t:this.shape_115},{t:this.shape_114},{t:this.shape_113},{t:this.shape_112},{t:this.shape_111},{t:this.shape_110},{t:this.shape_109},{t:this.shape_108},{t:this.shape_107},{t:this.shape_106},{t:this.shape_105},{t:this.shape_104},{t:this.shape_103},{t:this.shape_102},{t:this.shape_101},{t:this.shape_100},{t:this.shape_99},{t:this.shape_98},{t:this.shape_97},{t:this.shape_96},{t:this.shape_95},{t:this.shape_94},{t:this.shape_93},{t:this.shape_92},{t:this.shape_91},{t:this.shape_90},{t:this.shape_89},{t:this.shape_88},{t:this.shape_87},{t:this.shape_86},{t:this.shape_85},{t:this.shape_84},{t:this.shape_83},{t:this.shape_82},{t:this.shape_81},{t:this.shape_80},{t:this.shape_79},{t:this.shape_78},{t:this.shape_77},{t:this.shape_76},{t:this.shape_75},{t:this.shape_74},{t:this.shape_73},{t:this.shape_72},{t:this.shape_71},{t:this.shape_70},{t:this.shape_69},{t:this.shape_68},{t:this.shape_67},{t:this.shape_66},{t:this.shape_65},{t:this.shape_64},{t:this.shape_63},{t:this.shape_62},{t:this.shape_61},{t:this.shape_60},{t:this.shape_59},{t:this.shape_58},{t:this.shape_57},{t:this.shape_56},{t:this.shape_55},{t:this.shape_54},{t:this.shape_53},{t:this.shape_52},{t:this.shape_51},{t:this.shape_50},{t:this.shape_49},{t:this.shape_48},{t:this.shape_47},{t:this.shape_46},{t:this.shape_45},{t:this.shape_44},{t:this.shape_43},{t:this.shape_42},{t:this.shape_41},{t:this.shape_40},{t:this.shape_39},{t:this.shape_38},{t:this.shape_37},{t:this.shape_36},{t:this.shape_35},{t:this.shape_34},{t:this.shape_33},{t:this.shape_32},{t:this.shape_31},{t:this.shape_30},{t:this.shape_29},{t:this.shape_28},{t:this.shape_27},{t:this.shape_26},{t:this.shape_25},{t:this.shape_24},{t:this.shape_23},{t:this.shape_22},{t:this.shape_21},{t:this.shape_20},{t:this.shape_19},{t:this.shape_18},{t:this.shape_17},{t:this.shape_16},{t:this.shape_15},{t:this.shape_14},{t:this.shape_13},{t:this.shape_12},{t:this.shape_11},{t:this.shape_10},{t:this.shape_9},{t:this.shape_8},{t:this.shape_7},{t:this.shape_6},{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-275.1,-200.1,600,480);


(lib.factory = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 2
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FFFFFF").s().p("AqmglILXk+IJ2GDIr1FEg");
	this.shape.setTransform(3.5,-32.5);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#E8E8E8").s().p("Al6jlIL1lFIgCL/IrzFVg");
	this.shape_1.setTransform(33.5,26.2);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#000000").s().p("AkJKAIgElrIjsiYIABFrIiuhwIgFgCIgLsuILqlFIKCGNIgDMQIsCFdgAkDEQIAEFrICxB3IL4lYIACsEIp5mIIrfFBIALMhICfBlIgBlqg");
	this.shape_2.setTransform(3.4,6.8);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#F2F2F2").s().p("Aj/J7IgElrIkAilIABFrIifhmIgLshILflAIJ5GHIgCMEIr4FYg");
	this.shape_3.setTransform(3.4,6.8);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#000000").s().p("Ak9A2IHTjRICoBpInRDOgAknA3ICUBZIG7jDIiShcg");
	this.shape_4.setTransform(-32.7,39.1);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.lf(["#FF4AF7","#CF37C6","#941F8B","#690E5F","#4F0445","#45003B"],[0,0.204,0.478,0.71,0.894,1],8.5,6,-8.6,-5.9).s().p("Ak9A2IHTjRICoBpInRDOg");
	this.shape_5.setTransform(-32.7,39.1);

	this.shape_6 = new cjs.Shape();
	this.shape_6.graphics.f("#000000").s().p("AjUgfIGvjLIAPEDInTDSgAjLgZIgTD0IG+jIIgOjug");
	this.shape_6.setTransform(-41.1,21);

	this.shape_7 = new cjs.Shape();
	this.shape_7.graphics.lf(["#000000","#21001C","#3B0033","#45003B"],[0,0.384,0.773,1],0,-6.6,0,11.9).s().p("AjUgfIGvjLIAPEDInTDSg");
	this.shape_7.setTransform(-41.1,21);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_7},{t:this.shape_6},{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = getMCSymbolPrototype(lib.factory, new cjs.Rectangle(-66,-69.7,138.9,153.1), null);


(lib.dollarStackOrange = function(mode,startPosition,loop) {
if (loop == null) { loop = false; }	this.initialize(mode,startPosition,loop,{});

}).prototype = getMCSymbolPrototype(lib.dollarStackOrange, null, null);


(lib.dollarStackGreen = function(mode,startPosition,loop) {
if (loop == null) { loop = false; }	this.initialize(mode,startPosition,loop,{});

}).prototype = getMCSymbolPrototype(lib.dollarStackGreen, null, null);


(lib.dollarOrange = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("rgba(204,102,51,0.498)").s().p("Ah4AKICghHIBRA0IigBHgAhvALIBJAuICXhDIhJgugAhiAMICJg9IA8AmIiIA9gAAFAKIgPAHIAHAEIAOgGIAHAEIAHgDIgGgFIAHgDIgGgEIAHgDIgHgEIgHADIgHgEIgHAEIgFgFIANgGIgHgFIgNAIIgHgFIgIAEIAHADIgIAEIAHADIgIADIAIAFIAHgEIAGAFIAIgDgAAFADIAIgDIAGADIgHAEgAgVABIAHgCIAGADIgHADg");
	this.shape.setTransform(12.1,6.2);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#CC3333").s().p("AhwALICXhDIBKAuIiXBDgAhiAMIA9AmICIg9Ig9gmg");
	this.shape_1.setTransform(12.1,6.2);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#FFFFFF").s().p("AgIAOIAOgGIgGgEIgHADIgGgEIgIADIgHgEIAIgCIgHgFIAIgDIgHgEIAIgDIAGAEIAOgHIAHAEIgOAHIAFAEIAIgDIAGAEIAIgDIAHAEIgIADIAHADIgHAEIAGAEIgHADIgHgDIgOAGgAAHABIAHADIAHgDIgHgDgAgUAAIAHADIAHgDIgHgEg");
	this.shape_2.setTransform(11.9,6.4);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = getMCSymbolPrototype(lib.dollarOrange, new cjs.Rectangle(0,0,24.1,12.3), null);


(lib.dollarGrey = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#313131").s().p("AhwALICXhDIBKAuIiXBDgAhiAMIA8AmIABgBICIg8Ig9gmg");
	this.shape.setTransform(12.1,6.2);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#6A6A6A").s().p("Ah4AKICghHIBRA0IigBHgAhvALIBJAuICXhDIhJgugAhiAMICJg9IA8AmIiIA9IgBAAgAAEAKIgOAHIAHAEIAOgGIAGAEIABAAIAFgDIACAAIgGgFIAHgDIgGgEIAHgDIgHgEIgHADIgHgEIgHAEIgGgFIAOgGIgHgEIAAgBIgNAIIgHgFIgBAAIgHAEIAHADIgIAEIAHADIgIADIAIAFIAHgEIAGAFIAIgDgAAFADIAIgDIAGADIgHAEgAgVABIAAAAIAHgCIAGADIgHADg");
	this.shape_1.setTransform(12.1,6.2);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#FFFFFF").s().p("AgIAOIAOgGIgGgEIgHADIgGgEIgIADIgHgEIAIgDIgHgEIAHgDIgGgEIAHgDIABAAIAGAEIAOgHIAAAAIAHAEIgOAHIAFAEIAIgDIAGAEIAIgDIAHAEIgIADIAHADIgHAEIAGAEIgCABIgGACIAAAAIgGgDIgOAGgAAHABIAHADIAHgDIgHgDgAgUgBIABABIAGADIAHgDIgHgEg");
	this.shape_2.setTransform(11.9,6.4);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = getMCSymbolPrototype(lib.dollarGrey, new cjs.Rectangle(0,0,24.1,12.3), null);


(lib.dollarGreen = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#628118").s().p("AhwALICXhDIBKAuIiXBDgAhiAMIA9AmICIg9Ig9gmg");
	this.shape.setTransform(12.1,6.2);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#FFFFFF").s().p("AgIAOIAOgGIgGgEIgHADIgGgEIgIADIgHgEIAIgCIgHgFIAIgDIgHgEIAIgDIAGAEIAOgHIAHAEIgOAHIAFAEIAIgDIAGAEIAIgDIAHAEIgIADIAHADIgHAEIAGAEIgHADIgHgDIgOAGgAAHABIAHADIAHgDIgHgDgAgUAAIAHADIAHgDIgHgEg");
	this.shape_1.setTransform(11.9,6.4);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#93AD3F").s().p("Ah4AKICghHIBRA0IigBHgAhvALIBJAuICXhDIhJgugAhiAMICJg9IA8AmIiIA9gAAFAKIgPAHIAHAEIAOgGIAHAEIAHgDIgGgFIAHgDIgGgEIAHgDIgHgEIgHADIgHgEIgHAEIgFgFIANgGIgHgFIgNAIIgHgFIgIAEIAHADIgIAEIAHADIgIADIAIAFIAHgEIAGAFIAIgDgAAFADIAIgDIAGADIgHAEgAgVABIAHgCIAGADIgHADg");
	this.shape_2.setTransform(12.1,6.2);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = getMCSymbolPrototype(lib.dollarGreen, new cjs.Rectangle(0,0,24.1,12.3), null);


(lib.conveyor = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#474747").s().p("AAeBSIAYg2IBdA4IAAACgAg+AaIAYg2IBcA4gAiChVIBcA5IhsADg");
	this.shape.setTransform(-66.3,88.8);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#474747").s().p("AAeBSIAYg2IBdA4IAAACgAg+AaIAYg2IBcA4gAiChVIBcA5IhsADg");
	this.shape_1.setTransform(179.4,-22.7);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#474747").s().p("AAkAcIBkgDIgPA7gAgxgaIBrACIgWA0gAiHhSIAAgBIBsADIgWA2g");
	this.shape_2.setTransform(123.7,-61.9);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#474747").s().p("AjmBfIAAAAIF8ipIgBAAIAAAAIBGgfQABAFADAEIABABIAGAgIhOgKIAHAqIhKgKIAIAoIhEgJIAHAjIg8gIIAGAgIhJgKIAHAoIhEgJIAHAkg");
	this.shape_3.setTransform(160.3,-62.8);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#474747").s().p("AjMBgIgDgtIBLAJIgDgoIBFAIIgDglIA9AIIgCgiIBJAJIgCgpIBDAJIgDgmIBSALIAAAAImaC2g");
	this.shape_4.setTransform(-139,73.8);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("rgba(163,163,163,0.902)").s().p("A5kMVIpCECIAnhHIiRAFIAmhGIiUADIAohHMAoPgR/Id2tkIEXCrIopD6IJiF/MgvaAVaImYCzgAzJJdIFSDVMAn8gSJIkzjRg");
	this.shape_5.setTransform(0.7,2.2);

	this.shape_6 = new cjs.Shape();
	this.shape_6.graphics.f("#474747").s().p("EgkJAQrICRgFIgnBHgEgkJAQrIhuhDICUgDIgmBGgEgl3APoIgxgfIBZgoIgoBHgEAg2gRCIBdgqIEWCsIhcApg");
	this.shape_6.setTransform(0,-6.5);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_6},{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = getMCSymbolPrototype(lib.conveyor, new cjs.Rectangle(-247.3,-119.8,494.7,239.7), null);


(lib.character = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#000000").s().p("AgQAAIABgTIAgATIgBAUg");
	this.shape.setTransform(7.7,52.9);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#000000").s().p("AgQAAIABgTIAgATIAAAUg");
	this.shape_1.setTransform(1.7,49.3);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#000000").s().p("AgNApIAChhIAZAQIgCBhg");
	this.shape_2.setTransform(5.6,7.7);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#000000").s().p("AgHA3IADh1IAMAIIgDB1g");
	this.shape_3.setTransform(6.8,45.4);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#000000").s().p("AgcBmIAFjrIA0AgIgFDrg");
	this.shape_4.setTransform(5.2,26.5);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#000000").s().p("AgHA3IADh1IAMAIIgDB1g");
	this.shape_5.setTransform(2.8,43);

	this.shape_6 = new cjs.Shape();
	this.shape_6.graphics.f("rgba(255,0,0,0)").s().p("AgzDaIALnrIBcA4IgLHrg");
	this.shape_6.setTransform(5.2,27.4);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_6},{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,10.4,54.9);


(lib.bubbleOrange = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 2
	this.label = new cjs.Text("10€", "32px 'Gotham Medium'", "#FFFFFF");
	this.label.name = "label";
	this.label.textAlign = "center";
	this.label.lineHeight = 30;
	this.label.parent = this;
	this.label.setTransform(38.6,31.8);

	this.timeline.addTween(cjs.Tween.get(this.label).wait(1));

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FF6600").s().p("ABLFVQgkAHgnAAQieAAhxhwQhwhwAAieQAAifBwhxQBxhwCeAAQCfAABwBwQBxBxgBCfQABCehxBwQgmAmgrAZIAAB4g");
	this.shape.setTransform(38.4,41.9);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

}).prototype = getMCSymbolPrototype(lib.bubbleOrange, new cjs.Rectangle(0,0,76.7,83.8), null);


(lib.bubbleGreen = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 2
	this.label = new cjs.Text("10€", "32px 'Gotham Medium'", "#FFFFFF");
	this.label.name = "label";
	this.label.textAlign = "center";
	this.label.lineHeight = 30;
	this.label.parent = this;
	this.label.setTransform(38.6,31.8);

	this.timeline.addTween(cjs.Tween.get(this.label).wait(1));

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#93AD40").s().p("ABLFVQgkAHgnAAQieAAhxhwQhwhwAAieQAAifBwhxQBxhwCeAAQCfAABwBwQBxBxgBCfQABCehxBwQgmAmgrAZIAAB4g");
	this.shape.setTransform(38.4,41.9);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

}).prototype = getMCSymbolPrototype(lib.bubbleGreen, new cjs.Rectangle(0,0,76.7,83.8), null);


(lib.bubbleBlue = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 2
	this.label = new cjs.Text("10€", "32px 'Gotham Medium'", "#FFFFFF");
	this.label.name = "label";
	this.label.textAlign = "center";
	this.label.lineHeight = 30;
	this.label.parent = this;
	this.label.setTransform(38.6,31.8);

	this.timeline.addTween(cjs.Tween.get(this.label).wait(1));

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#0099FF").s().p("Ai8ErQgsgZgmgmQhwhwgBieQABifBwhxQBwhwCeAAQCfAABxBwQBvBxAACfQAACehvBwQhxBwifAAQgmAAglgGIhxBNg");
	this.shape.setTransform(38.4,41.9);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

}).prototype = getMCSymbolPrototype(lib.bubbleBlue, new cjs.Rectangle(0,0,76.7,83.8), null);


(lib.cart = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 2
	this.bubble = new lib.bubbleBlue();
	this.bubble.parent = this;
	this.bubble.setTransform(82.9,-17.5,0.642,0.55,0,0,31,38.4,41.9);
	this.bubble.alpha = 0;

	this.timeline.addTween(cjs.Tween.get(this.bubble).wait(1));

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#000000").s().p("Ak0AaIGXi0IDSCCImZCzgAkpAbIDFB6IGOiuIjIh7g");
	this.shape.setTransform(30.9,15.5);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#FFFFFF").s().p("Ak0AbIGXi1IDSCCImZCzg");
	this.shape_1.setTransform(30.9,15.5);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#000000").s().p("AjMBDIGZizIAAAtImZCzgAjHBHIAAAiIGPivIAAgig");
	this.shape_2.setTransform(41.2,24.3);

	this.shape_3 = new cjs.Shape();
	this.shape_3.graphics.f("#A3A3A3").s().p("AjMBDIGZizIAAAtImZCzg");
	this.shape_3.setTransform(41.2,24.3);

	this.shape_4 = new cjs.Shape();
	this.shape_4.graphics.f("#000000").s().p("AhngqIAAgsIDPCAIAAAtgAhigtIDFB7IAAghIjFh6g");
	this.shape_4.setTransform(10.4,26.8);

	this.shape_5 = new cjs.Shape();
	this.shape_5.graphics.f("#FFFFFF").s().p("AhngqIAAgsIDPCAIAAAtg");
	this.shape_5.setTransform(10.4,26.8);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_5},{t:this.shape_4},{t:this.shape_3},{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = getMCSymbolPrototype(lib.cart, new cjs.Rectangle(0,-53.2,103.9,88.8), null);


// stage content:
(lib.trust_simulation = function(mode,startPosition,loop) {
if (loop == null) { loop = false; }	this.initialize(mode,startPosition,loop,{init:4,start:54,first_move:85,second_move:192});

	// timeline functions:
	this.frame_34 = function() {
		if (window) {
			/**
			 * Define/get default values.
			 */
			var startAmount = 10;
			var multiplier = 3;
			var labelA = 'participant A';
			var labelB = 'participant B';
			var currency = '€';
			var locale = 'fr';
		
			if (document) {
				var canvas = document.getElementsByTagName('canvas')[0];
				if (canvas) {
					labelA = canvas.getAttribute('data-participants-label-a') || labelA;
					labelB = canvas.getAttribute('data-participants-label-b') || labelB;
					multiplier = canvas.getAttribute('data-multiplier') || multiplier;
					startAmount = canvas.getAttribute('data-start-amount') || startAmount;
					currency = canvas.getAttribute('data-currency') || currency;
					locale = canvas.getAttribute('data-locale') || locale;
				}
			}
			
			function setMoneyText(money) {
				return currency + money.toString();
			}
			
			function createDollar(color) {
				switch (color) {
					case 'green': 
						dollar = new lib.dollarGreen;
						break;
					case 'orange':
						dollar = new lib.dollarOrange;
						break;
					case 'grey':
						dollar = new lib.dollarGrey;
						break;
				}
				
				return dollar;
			}
		
			/**
			 * Operations on carts.
			 */
			var carts = function () {
				var X_OFFSET = 18;
				var Y_OFFSET = 9;
				var Z_OFFSET = 3;
				
				this.cart1.bubble.alpha = 0;
				this.cart2.bubble.alpha = 0;
				
				var pushMoney = function(cart, dollar) {
					cart.money++;
					if (locale === 'ko') {
						if (cart.money % 1000 === 0) {
							cart.stack.push(dollar);
							cart.instance.addChild(dollar);
						}
					} else {
						cart.stack.push(dollar);
						cart.instance.addChild(dollar);
					}
					cart.instance.bubble.alpha = 1;
					cart.instance.bubble.label.text = currency + cart.money.toString();
				}
				
				var popMoney = function(cart) {
					if (cart.stack.length > 0) {
						cart.money--;
						cart.instance.bubble.label.text = currency + cart.money.toString();
						if (locale === 'ko') {
							if (cart.money % 1000 === 0) {
								cart.instance.removeChild(cart.stack.pop());
							}				
						} else {
							cart.instance.removeChild(cart.stack.pop());
						}
						return true;
					}
				}
				
				if (locale === 'ko') {
					this.cart1.bubble.label.font = "18px 'Gotham Medium'";
					this.cart2.bubble.label.font = "18px 'Gotham Medium'";
				}
		
				var carts = [{
					money: 0,
					color: '',
					instance: this.cart1,
					stack: []
				}, {
					money: 0,
					color: '',
					instance: this.cart2,
					stack: []
				}];
		
				var increment = function (cartIndex, color) {
					var cart = carts[cartIndex];
					var dollar = createDollar(color);
					
					dollar.x = X_OFFSET;
					dollar.y = Y_OFFSET - Z_OFFSET * cart.stack.length;
					
					pushMoney(cart, dollar);
					return this;
				}.bind(this);
				
				var decrement = function (cartIndex) {
					var cart = carts[cartIndex];
					popMoney(cart);
					return this;
				}.bind(this);
				
				var batchRemove = function (cartIndex) {
					var total = carts[cartIndex].money;
					var i = total;
					while (i > 0) {
						decrement(cartIndex);
						i--;
					}
					return total;
				}
				
				var batchAdd = function (cartIndex, amount, color) {
					for (var i = 0; i < amount; i++) {
						increment(cartIndex, color);
					}
				}
				
				var move = function (cartIndex) {
					if (cartIndex === 0) {
						this.gotoAndPlay('first_move');
					} else {
						this.gotoAndPlay('second_move');
						var self = this;
						setTimeout(function () {
							self.cart1.bubble.alpha = 0;
							self.cart2.bubble.alpha = 0;
						}, 2000);
					}
					return this;
				}.bind(this);
				
				var multiplyMoney = function (cartIndex, multiplier) {
					window.TRUST.multipliedMoney = carts[cartIndex].money * multiplier;
					batchRemove(cartIndex);
					batchAdd(cartIndex, window.TRUST.multipliedMoney, 'grey');
				}
				
				var reset = function () {
					this.cart1.bubble.alpha = 0;
					this.cart2.bubble.alpha = 0;
					carts[0].money = 0;
					carts[0].color = '';
					carts[0].stack = [];
					carts[1].money = 0;
					carts[0].color = '';
					carts[0].stack = [];
				}.bind(this);
		
				return {
					increment: increment,
					decrement: decrement,
					move: move,
					multiply: multiplyMoney,
					removeAll: batchRemove,
					reset: reset,
					carts: carts
				}
			}.bind(this);
		
			/**
			 * Operations on players.
			 */
			var players = function () {
				var X_OFFSET = 0;
				var Y_OFFSET = 22.5;
				var Z_OFFSET = 2.5;
				
				var players = [{
					money: 0,
					instance: this.stack1,
					stack: []
				}, {
					money: 0,
					instance: this.stack2,
					stack: []
				}];
				
				if (locale === 'ko') {
					this.bubble1.label.font = "18px 'Gotham Medium'";
					this.bubble2.label.font = "18px 'Gotham Medium'";
				}
				
				this.charLabel1.label.text = labelA;
				this.charLabel2.label.text = labelB;
				
				var pushMoney = function(player, dollar, playerIndex) {
					player.money++;
					if (locale === 'ko') {
						if (player.money % 1000 === 0) {
							player.stack.push(dollar);
							player.instance.addChild(dollar);
						}
					} else {
						player.stack.push(dollar);
						player.instance.addChild(dollar);
					}
					var bubble = playerIndex === 0 ? this.bubble1 : this.bubble2;
					bubble.label.text = setMoneyText(player.money.toString());
					return this;
				}.bind(this);
				
				var popMoney = function(player, playerIndex) {
					if (player.money > 0) {
						player.money--;
						
						var bubble = playerIndex === 0 ? this.bubble1 : this.bubble2;
						bubble.label.text = setMoneyText(player.money.toString());
						
						if (locale === 'ko') {
							if (player.money % 1000 === 0) {
								player.instance.removeChild(player.stack.pop());
							}
						} else {
							player.instance.removeChild(player.stack.pop());
						}
					}
					return this;
				}.bind(this);
		
				var increment = function (i, moneyColor, force) {
					var p = players[i];
						
					var dollar = createDollar(moneyColor);
					dollar.x = X_OFFSET;
					dollar.y = Y_OFFSET - Z_OFFSET * p.stack.length;
					
					pushMoney(p, dollar, i);
					return this;
				}.bind(this);
		
				var decrement = function (i) {
					popMoney(players[i], i);
					return this;
				}.bind(this);
				
				var reset = function () {
					while (players[0].stack.length > 0) {
						decrement(0);
					}
					
					while (players[1].stack.length > 0) {
						decrement(1);
					}
					
					for (var i = 0; i < players.length; i++) {
						var colors = ['green', 'orange'];
						while (players[i].money < startAmount) {
							increment(i, colors[i]);
						}
					}
				}.bind(this);
				
				var getMaxPlayer1Money = function () {
					return players[0].money;
				}.bind(this);
				
				var getMaxPlayer2Money = function () {
					return players[1].money;
				}.bind(this);
				
				reset();
		
				return {
					increment: increment,
					decrement: decrement,
					reset: reset,
					getMaxPlayer1Money: getMaxPlayer1Money,
					getMaxPlayer2Money: getMaxPlayer2Money
				}
			}.bind(this);
			
			/**
			 * API mixing operations.
			 */
			var playersControls = players();
			var cartsControls = carts();
			
			var operate = function (p, c) {
				var players = p;
				var carts = c;
				
				var playerPutsOwnMoney = function (playerIndex, cartIndex, moneyColor) {
					players.decrement(playerIndex);
					
					var color = moneyColor ? moneyColor : (playerIndex === 0 ? 'green' : 'orange')
					carts.increment(cartIndex, color);
				}
				
				var playerTakesMoney = function (playerIndex, cartIndex, moneyColor) {
					players.increment(playerIndex, moneyColor);
					carts.decrement(cartIndex);
				}
				
				var moveCart1 = function () {
					carts.move(0);
				}
				
				var moveCart2 = function () {
					carts.move(1);
				}
				
				var incrementFromCartToCart = function(from, to) {
					if (carts.decrement(from)) {
						carts.increment(to, 'grey');
					}
				}
				
				var decrementFromCartToCart = function(from, to) {
					if (carts.decrement(to)) {
						carts.increment(from, 'grey');
					}
				}
				
				var passInFactory = function () {
					carts.multiply(0, multiplier);
				}
				
				var dispatchFinalGains = function () {
					var giveToPlayer1 = carts.removeAll(1);
					for (var i = 0; i < giveToPlayer1; i++) {
						players.increment(0, 'grey');
					}
					
					var giveToPlayer2 = carts.removeAll(0);
					for (var j = 0; j < giveToPlayer2; j++) {
						players.increment(1, 'grey', true);
					}
				}
				
				var getMaxCart1Money = function () {
					return carts.carts[0].money;
				}
				
				var getMaxCart2Money = function () {
					return carts.carts[1].money;
				}
				
				var getMaxPlayer1Money = function () {
					return players.getMaxPlayer1Money();
				}
				
				var getMaxPlayer2Money = function () {
					return players.getMaxPlayer2Money();
				}
				
				return {
					playerPutsOwnMoney: playerPutsOwnMoney,
					playerTakesMoney: playerTakesMoney,
					moveCart1: moveCart1,
					moveCart2: moveCart2,
					passInFactory: passInFactory,
					incrementFromCartToCart: incrementFromCartToCart,
					decrementFromCartToCart: decrementFromCartToCart,
					dispatchFinalGains: dispatchFinalGains,
					
					getMaxCart1Money: getMaxCart1Money,
					getMaxCart2Money: getMaxCart2Money,
					getMaxPlayer1Money: getMaxPlayer1Money,
					getMaxPlayer2Money: getMaxPlayer2Money
				}
			}.bind(this);
			
			var reset = function () {
				this.gotoAndPlay('start');
				playersControls.reset();
				cartsControls.reset();
			}.bind(this);
		
			var init = function () {
				return {
					operate: operate(playersControls, cartsControls),
					reset: reset
				}
			}.bind(this)
		
			var TRUST = init();
			window.TRUST = TRUST;
		}
	}
	this.frame_84 = function() {
		this.stop();
	}
	this.frame_123 = function() {
		window.TRUST.operate.passInFactory();
	}
	this.frame_191 = function() {
		this.stop();
	}
	this.frame_234 = function() {
		this.stop();
		window.TRUST.operate.dispatchFinalGains();
	}
	this.frame_339 = function() {
		this.stop();
		window.TRUST.operate.dispatchFinalGains();
	}
	this.frame_409 = function() {
		this.gotoAndPlay('start');
	}

	// actions tween:
	this.timeline.addTween(cjs.Tween.get(this).wait(34).call(this.frame_34).wait(50).call(this.frame_84).wait(39).call(this.frame_123).wait(68).call(this.frame_191).wait(43).call(this.frame_234).wait(105).call(this.frame_339).wait(70).call(this.frame_409).wait(1));

	// multiplier
	this.bubbleMultiplier = new lib.multiplier();
	this.bubbleMultiplier.parent = this;
	this.bubbleMultiplier.setTransform(274.1,205,0.141,0.161,0,0,32.7);
	this.bubbleMultiplier.alpha = 0;

	this.timeline.addTween(cjs.Tween.get(this.bubbleMultiplier).wait(119).to({scaleX:0.88,scaleY:1,skewY:32.6,y:163.4,alpha:1},4,cjs.Ease.get(1)).to({scaleX:0.88,y:141.7},28).to({scaleX:0.88,skewY:32.7,y:139,alpha:0},3).to({_off:true},146).wait(110));

	// chariot 2
	this.cart2 = new lib.cart();
	this.cart2.parent = this;
	this.cart2.setTransform(495.2,222,0.87,0.87,0,0,0,30.8,17.8);
	this.cart2.alpha = 0;
	this.cart2._off = true;

	this.timeline.addTween(cjs.Tween.get(this.cart2).wait(74).to({_off:false},0).to({alpha:1},5,cjs.Ease.get(1)).wait(113).to({x:522.6,y:241.9},5,cjs.Ease.get(1)).to({x:223.6,y:375.9},32,cjs.Ease.get(1)).to({x:162.3,y:338.5},5).wait(176));

	// Calque 1 (mask)
	var mask = new cjs.Shape();
	mask._off = true;
	mask.graphics.p("AmYKFIAAmQImykDIh+goIAArQIHgi0QDUgUDagIQFugOFUBdQAhAJAQAcQFmKIhyLxIv7HCg");
	mask.setTransform(314.9,241.5);

	// factory front
	this.instance = new lib.factory();
	this.instance.parent = this;
	this.instance.setTransform(300,-80,1,1,0,0,0,3.4,6.8);
	this.instance._off = true;

	var maskedShapeInstanceList = [this.instance];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(4).to({_off:false},0).to({y:240},5,cjs.Ease.get(1)).wait(401));

	// bubble 2
	this.bubble2 = new lib.bubbleOrange();
	this.bubble2.parent = this;
	this.bubble2.setTransform(432.8,117.3,0.086,0.073,0,0,32,38.6,42);
	this.bubble2.alpha = 0;

	this.timeline.addTween(cjs.Tween.get(this.bubble2).wait(77).to({alpha:1},0).to({regX:38.3,regY:41.8,scaleX:0.79,scaleY:0.67,x:413.8,y:100.2},7).wait(170).to({regX:38.6,regY:42,scaleX:0.09,scaleY:0.07,x:432.8,y:117.3},5,cjs.Ease.get(1)).to({_off:true},1).wait(150));

	// dollar stack (orange)
	this.stack2 = new lib.dollarStackOrange();
	this.stack2.parent = this;
	this.stack2.setTransform(422.7,180.9,1,1,0,0,0,12.1,17.4);
	this.stack2._off = true;

	this.timeline.addTween(cjs.Tween.get(this.stack2).wait(82).to({_off:false},0).wait(328));

	// char labels
	this.charLabel2 = new lib.participantLabel();
	this.charLabel2.parent = this;
	this.charLabel2.setTransform(458.3,110.8,1,1,-56.4,0,0,51.7,30.9);

	this.charLabel1 = new lib.participantLabel();
	this.charLabel1.parent = this;
	this.charLabel1.setTransform(161.9,245,1,1,-56.4,0,0,51.7,30.9);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[]}).to({state:[{t:this.charLabel1},{t:this.charLabel2}]},34).to({state:[{t:this.charLabel1},{t:this.charLabel2}]},115).wait(261));

	// bubble 1
	this.bubble1 = new lib.bubbleGreen();
	this.bubble1.parent = this;
	this.bubble1.setTransform(131.1,259.4,0.083,0.07,0,0,32,38.4,42.1);
	this.bubble1.alpha = 0;

	this.timeline.addTween(cjs.Tween.get(this.bubble1).wait(77).to({alpha:1},0).to({regX:38.3,regY:41.8,scaleX:0.79,scaleY:0.67,x:114.1,y:229.3},7,cjs.Ease.get(1)).to({_off:true},187).wait(139));

	// dollarGrey
	this.instance_1 = new lib.dollarGrey();
	this.instance_1.parent = this;
	this.instance_1.setTransform(262,594,1,1,0,0,0,12.1,6.2);

	this.timeline.addTween(cjs.Tween.get(this.instance_1).wait(410));

	// d1 copy 10
	this.instance_2 = new lib.dollarOrange("synched",0);
	this.instance_2.parent = this;
	this.instance_2.setTransform(422.7,-130.3,1,1,0,0,0,12.1,6.2);
	this.instance_2._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_2).wait(46).to({_off:false},0).to({y:169.7},8,cjs.Ease.get(1)).to({_off:true},29).wait(327));

	// d1 copy 11
	this.instance_3 = new lib.dollarOrange("synched",0);
	this.instance_3.parent = this;
	this.instance_3.setTransform(422.7,-127.8,1,1,0,0,0,12.1,6.2);
	this.instance_3._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_3).wait(45).to({_off:false},0).to({y:172.2},8,cjs.Ease.get(1)).to({_off:true},30).wait(327));

	// d1 copy 12
	this.instance_4 = new lib.dollarOrange("synched",0);
	this.instance_4.parent = this;
	this.instance_4.setTransform(422.7,-125.3,1,1,0,0,0,12.1,6.2);
	this.instance_4._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_4).wait(44).to({_off:false},0).to({y:174.7},8,cjs.Ease.get(1)).to({_off:true},31).wait(327));

	// d1 copy 13
	this.instance_5 = new lib.dollarOrange("synched",0);
	this.instance_5.parent = this;
	this.instance_5.setTransform(422.7,-122.8,1,1,0,0,0,12.1,6.2);
	this.instance_5._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_5).wait(43).to({_off:false},0).to({y:177.2},8,cjs.Ease.get(1)).to({_off:true},32).wait(327));

	// d1 copy 14
	this.instance_6 = new lib.dollarOrange("synched",0);
	this.instance_6.parent = this;
	this.instance_6.setTransform(422.7,-120.3,1,1,0,0,0,12.1,6.2);
	this.instance_6._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_6).wait(42).to({_off:false},0).to({y:179.7},8,cjs.Ease.get(1)).to({_off:true},33).wait(327));

	// d1 copy 15
	this.instance_7 = new lib.dollarOrange("synched",0);
	this.instance_7.parent = this;
	this.instance_7.setTransform(422.7,-117.8,1,1,0,0,0,12.1,6.2);
	this.instance_7._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_7).wait(41).to({_off:false},0).to({y:182.2},8,cjs.Ease.get(1)).to({_off:true},34).wait(327));

	// d1 copy 16
	this.instance_8 = new lib.dollarOrange("synched",0);
	this.instance_8.parent = this;
	this.instance_8.setTransform(422.7,-115.3,1,1,0,0,0,12.1,6.2);
	this.instance_8._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_8).wait(40).to({_off:false},0).to({y:184.7},8,cjs.Ease.get(1)).to({_off:true},35).wait(327));

	// d1 copy 17
	this.instance_9 = new lib.dollarOrange("synched",0);
	this.instance_9.parent = this;
	this.instance_9.setTransform(422.7,-112.8,1,1,0,0,0,12.1,6.2);
	this.instance_9._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_9).wait(39).to({_off:false},0).to({y:187.2},8,cjs.Ease.get(1)).to({_off:true},36).wait(327));

	// d1 copy 18
	this.instance_10 = new lib.dollarOrange("synched",0);
	this.instance_10.parent = this;
	this.instance_10.setTransform(422.7,-110.3,1,1,0,0,0,12.1,6.2);
	this.instance_10._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_10).wait(38).to({_off:false},0).to({y:189.7},8,cjs.Ease.get(1)).to({_off:true},37).wait(327));

	// d1 copy 19
	this.instance_11 = new lib.dollarOrange("synched",0);
	this.instance_11.parent = this;
	this.instance_11.setTransform(422.7,-107.8,1,1,0,0,0,12.1,6.2);
	this.instance_11._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_11).wait(37).to({_off:false},0).to({y:192.2},8,cjs.Ease.get(1)).to({_off:true},38).wait(327));

	// dollar stack (green)
	this.stack1 = new lib.dollarStackGreen();
	this.stack1.parent = this;
	this.stack1.setTransform(118.3,316.1,1,1,0,0,0,12.1,17.4);
	this.stack1._off = true;

	this.timeline.addTween(cjs.Tween.get(this.stack1).wait(82).to({_off:false},0).wait(328));

	// d1 copy 5
	this.instance_12 = new lib.dollarGreen("synched",0);
	this.instance_12.parent = this;
	this.instance_12.setTransform(118.3,-35.1,1,1,0,0,0,12.1,6.2);
	this.instance_12._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_12).wait(41).to({_off:false},0).to({y:304.9},8,cjs.Ease.get(1)).to({_off:true},34).wait(327));

	// d1 copy 6
	this.instance_13 = new lib.dollarGreen("synched",0);
	this.instance_13.parent = this;
	this.instance_13.setTransform(118.3,-32.6,1,1,0,0,0,12.1,6.2);
	this.instance_13._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_13).wait(40).to({_off:false},0).to({y:307.4},8,cjs.Ease.get(1)).to({_off:true},35).wait(327));

	// d1 copy 7
	this.instance_14 = new lib.dollarGreen("synched",0);
	this.instance_14.parent = this;
	this.instance_14.setTransform(118.3,-30.1,1,1,0,0,0,12.1,6.2);
	this.instance_14._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_14).wait(39).to({_off:false},0).to({y:309.9},8,cjs.Ease.get(1)).to({_off:true},36).wait(327));

	// d1 copy 8
	this.instance_15 = new lib.dollarGreen("synched",0);
	this.instance_15.parent = this;
	this.instance_15.setTransform(118.3,-27.6,1,1,0,0,0,12.1,6.2);
	this.instance_15._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_15).wait(38).to({_off:false},0).to({y:312.4},8,cjs.Ease.get(1)).to({_off:true},37).wait(327));

	// d1 copy 9
	this.instance_16 = new lib.dollarGreen("synched",0);
	this.instance_16.parent = this;
	this.instance_16.setTransform(118.3,-25.1,1,1,0,0,0,12.1,6.2);
	this.instance_16._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_16).wait(37).to({_off:false},0).to({y:314.9},8,cjs.Ease.get(1)).to({_off:true},38).wait(327));

	// d1 copy 4
	this.instance_17 = new lib.dollarGreen("synched",0);
	this.instance_17.parent = this;
	this.instance_17.setTransform(118.3,-22.6,1,1,0,0,0,12.1,6.2);
	this.instance_17._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_17).wait(36).to({_off:false},0).to({y:317.4},8,cjs.Ease.get(1)).to({_off:true},39).wait(327));

	// d1 copy 3
	this.instance_18 = new lib.dollarGreen("synched",0);
	this.instance_18.parent = this;
	this.instance_18.setTransform(118.3,-20.1,1,1,0,0,0,12.1,6.2);
	this.instance_18._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_18).wait(35).to({_off:false},0).to({y:319.9},8,cjs.Ease.get(1)).to({_off:true},40).wait(327));

	// d1 copy 2
	this.instance_19 = new lib.dollarGreen("synched",0);
	this.instance_19.parent = this;
	this.instance_19.setTransform(118.3,-17.6,1,1,0,0,0,12.1,6.2);
	this.instance_19._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_19).wait(34).to({_off:false},0).to({y:322.4},8,cjs.Ease.get(1)).to({_off:true},41).wait(327));

	// d1 copy
	this.instance_20 = new lib.dollarGreen("synched",0);
	this.instance_20.parent = this;
	this.instance_20.setTransform(118.3,-15.1,1,1,0,0,0,12.1,6.2);
	this.instance_20._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_20).wait(32).to({_off:false},0).to({y:324.9},8,cjs.Ease.get(1)).to({_off:true},43).wait(327));

	// d1
	this.instance_21 = new lib.dollarGreen("synched",0);
	this.instance_21.parent = this;
	this.instance_21.setTransform(118.3,-12.6,1,1,0,0,0,12.1,6.2);
	this.instance_21._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_21).wait(31).to({_off:false},0).to({y:327.4},8,cjs.Ease.get(1)).to({_off:true},44).wait(327));

	// chariot 1
	this.cart1 = new lib.cart();
	this.cart1.parent = this;
	this.cart1.setTransform(163,338.8,0.775,0.775,0,0,0,30.9,17.8);
	this.cart1.alpha = 0;
	this.cart1._off = true;

	this.timeline.addTween(cjs.Tween.get(this.cart1).wait(74).to({_off:false},0).to({regX:30.8,scaleX:0.87,scaleY:0.87,x:162.9,alpha:1},5,cjs.Ease.get(1)).wait(10).to({x:286.9,y:282.8},30,cjs.Ease.get(1)).wait(35).to({mode:"synched",startPosition:0},0).to({x:465.9,y:201.8},35,cjs.Ease.get(1)).wait(110).to({scaleX:1,scaleY:1},0).to({scaleX:0.87,scaleY:0.87,x:524.4,y:238.6},10,cjs.Ease.get(1)).wait(5).to({startPosition:0},0).to({x:226.4,y:376.6},10,cjs.Ease.get(1)).wait(5).to({startPosition:0},0).to({x:164.2,y:337.1},10,cjs.Ease.get(1)).wait(71));

	// char 2
	this.instance_22 = new lib.character("synched",0);
	this.instance_22.parent = this;
	this.instance_22.setTransform(444.6,-182,1,1,0,0,0,5.2,27.4);
	this.instance_22._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_22).wait(32).to({_off:false},0).to({y:158},10,cjs.Ease.get(1)).wait(368));

	// char 1
	this.instance_23 = new lib.character("synched",0);
	this.instance_23.parent = this;
	this.instance_23.setTransform(137.7,-36.4,1,1,0,0,0,5.2,27.4);
	this.instance_23._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_23).wait(29).to({_off:false},0).to({y:293.6},10,cjs.Ease.get(1)).wait(371));

	// conveyor belt
	this.instance_24 = new lib.conveyor();
	this.instance_24.parent = this;
	this.instance_24.setTransform(318.6,276);
	this.instance_24.alpha = 0;
	this.instance_24._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_24).wait(9).to({_off:false},0).to({alpha:1},5,cjs.Ease.get(1)).wait(396));

	// factory back
	this.instance_25 = new lib.factory();
	this.instance_25.parent = this;
	this.instance_25.setTransform(300,-80,1,1,0,0,0,3.4,6.8);
	this.instance_25._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_25).wait(4).to({_off:false},0).to({y:240},5,cjs.Ease.get(1)).wait(401));

	// floor
	this.instance_26 = new lib.floor("synched",0);
	this.instance_26.parent = this;
	this.instance_26.setTransform(280.1,239.5,1,1,0,0,0,4.4,40);

	this.timeline.addTween(cjs.Tween.get(this.instance_26).wait(410));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(300.6,239.4,600,600.8);
// library properties:
lib.properties = {
	width: 600,
	height: 480,
	fps: 30,
	color: "#CCD1DB",
	opacity: 1.00,
	webfonts: {},
	manifest: [],
	preloads: []
};




})(lib = lib||{}, images = images||{}, createjs = createjs||{}, ss = ss||{}, AdobeAn = AdobeAn||{});
var lib, images, createjs, ss, AdobeAn;