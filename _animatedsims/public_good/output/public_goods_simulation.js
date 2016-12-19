(function (lib, img, cjs, ss, an) {

var p; // shortcut to reference prototypes
lib.ssMetadata = [];


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


(lib.multiplier = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.label = new cjs.Text("×", "bold 40px 'Gotham Bold'");
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


(lib.bubbleBlack = function(mode,startPosition,loop) {
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
	this.shape.graphics.f("#000000").s().p("Ai8ErQgsgZgmgmQhwhwgBieQABifBwhxQBwhwCeAAQCfAABxBwQBvBxAACfQAACehvBwQhxBwifAAQgmAAglgGIhxBNg");
	this.shape.setTransform(38.4,41.9);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

}).prototype = getMCSymbolPrototype(lib.bubbleBlack, new cjs.Rectangle(0,0,76.7,83.8), null);


(lib.dollarRed = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#990000").s().p("AhwALICXhDIBKAuIiXBDgAhiAMIA9AmICIg9Ig9gmg");
	this.shape.setTransform(12.1,6.2);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#CC3366").s().p("Ah4AKICghHIBRA0IigBHgAhvALIBJAuICXhDIhJgugAhiAMICJg9IA8AmIiIA9gAAFAKIgPAHIAHAEIAOgGIAHAEIAHgDIgGgFIAHgDIgGgEIAHgDIgHgEIgHADIgHgEIgHAEIgFgFIANgGIgHgFIgNAIIgHgFIgIAEIAHADIgIAEIAHADIgIADIAIAFIAHgEIAGAFIAIgDgAAFADIAIgDIAGADIgHAEgAgVABIAHgCIAGADIgHADg");
	this.shape_1.setTransform(12.1,6.2);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#FFFFFF").s().p("AgIAOIAOgGIgGgEIgHADIgGgEIgIADIgHgEIAIgCIgHgFIAIgDIgHgEIAIgDIAGAEIAOgHIAHAEIgOAHIAFAEIAIgDIAGAEIAIgDIAHAEIgIADIAHADIgHAEIAGAEIgHADIgHgDIgOAGgAAHABIAHADIAHgDIgHgDgAgUAAIAHADIAHgDIgHgEg");
	this.shape_2.setTransform(11.9,6.4);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,24.1,12.3);


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

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,24.1,12.3);


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

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,24.1,12.3);


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

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,24.1,12.3);


(lib.dollarBlue = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#0033FF").s().p("AhwALICXhDIBKAuIiXBDgAhiAMIA9AmICIg9Ig9gmg");
	this.shape.setTransform(12.1,6.2);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#00BACC").s().p("Ah4AKICghHIBRA0IigBHgAhvALIBJAuICXhDIhJgugAhiAMICJg9IA8AmIiIA9gAAFAKIgPAHIAHAEIAOgGIAHAEIAHgDIgGgFIAHgDIgGgEIAHgDIgHgEIgHADIgHgEIgHAEIgFgFIANgGIgHgFIgNAIIgHgFIgIAEIAHADIgIAEIAHADIgIADIAIAFIAHgEIAGAFIAIgDgAAFADIAIgDIAGADIgHAEgAgVABIAHgCIAGADIgHADg");
	this.shape_1.setTransform(12.1,6.2);

	this.shape_2 = new cjs.Shape();
	this.shape_2.graphics.f("#FFFFFF").s().p("AgIAOIAOgGIgGgEIgHADIgGgEIgIADIgHgEIAIgCIgHgFIAIgDIgHgEIAIgDIAGAEIAOgHIAHAEIgOAHIAFAEIAIgDIAGAEIAIgDIAHAEIgIADIAHADIgHAEIAGAEIgHADIgHgDIgOAGgAAHABIAHADIAHgDIgHgDgAgUAAIAHADIAHgDIgHgEg");
	this.shape_2.setTransform(11.9,6.4);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_2},{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,24.1,12.3);


(lib.conveyor = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("rgba(163,163,163,0.902)").s().p("ADVDzMgoOgR+IgohGICUADIgnhHICSAFIgnhHMBHrAgEIkXCrg");
	this.shape.setTransform(-28.3,-30.3);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#474747").s().p("EAg2ARDIEXirIBcApIkWCsgEgmogPIIAxgfIBuhDIBqhCIAnBHIiRgFIAmBGIiUgDIAoBHg");
	this.shape_1.setTransform(-26.2,-28.2);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-273.5,-141.5,494.7,226.7);


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


(lib.bubbleRed = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 2
	this.label = new cjs.Text("10€", "20px 'Gotham Medium'", "#FFFFFF");
	this.label.name = "label";
	this.label.textAlign = "center";
	this.label.lineHeight = 20;
	this.label.parent = this;
	this.label.setTransform(38.6,31.8);

	this.timeline.addTween(cjs.Tween.get(this.label).wait(1));

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#FF0000").s().p("ABLFVQgkAHgnAAQieAAhxhwQhwhwAAieQAAifBwhxQBxhwCeAAQCfAABwBwQBxBxgBCfQABCehxBwQgmAmgrAZIAAB4g");
	this.shape.setTransform(38.4,41.9);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

}).prototype = getMCSymbolPrototype(lib.bubbleRed, new cjs.Rectangle(0,0,76.7,83.8), null);


(lib.bubbleOrange = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 2
	this.label = new cjs.Text("10€", "20px 'Gotham Medium'", "#FFFFFF");
	this.label.name = "label";
	this.label.textAlign = "center";
	this.label.lineHeight = 20;
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
	this.label = new cjs.Text("10€", "20px 'Gotham Medium'", "#FFFFFF");
	this.label.name = "label";
	this.label.textAlign = "center";
	this.label.lineHeight = 20;
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
	this.label = new cjs.Text("10€", "20px 'Gotham Medium'", "#FFFFFF");
	this.label.name = "label";
	this.label.textAlign = "center";
	this.label.lineHeight = 20;
	this.label.parent = this;
	this.label.setTransform(38.6,31.8);

	this.timeline.addTween(cjs.Tween.get(this.label).wait(1));

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f("#0099FF").s().p("Ai8ErQgsgZgmgmQhwhwgBieQABifBwhxQBwhwCeAAQCfAABxBwQBvBxAACfQAACehvBwQhxBwifAAQgmAAglgGIhxBNg");
	this.shape.setTransform(38.4,41.9);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(1));

}).prototype = getMCSymbolPrototype(lib.bubbleBlue, new cjs.Rectangle(0,0,76.7,83.8), null);


(lib.arrowRed = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f().s("#CC3367").ss(3,1,0,3).p("EggOgHCQSVLKJnB1QJmB0GehLQGehMFvikQFvilChhJ");
	this.shape.setTransform(213.3,49.8);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#CC3367").s().p("Ag5gnIB/AQIhGAeIhFAhg");
	this.shape_1.setTransform(7,4);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,421.1,96.5);


(lib.arrowOrange = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f().s("#CD7448").ss(3,1,0,3).p("AxfB/IB+A6QBfAoDdAsQDdAsFVhgQFUhhFvikQFvikChhK");
	this.shape.setTransform(119,28.3);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#CD7448").s().p("Ag5gmIB/APIhGAeIhFAhg");
	this.shape_1.setTransform(7,40.3);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,-1.5,232.5,59.7);


(lib.arrowGreen = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f().s("#93AD40").ss(3,1,0,3).p("AI2rsQjeBpk+CbQk+CbiZDnQiaDlAsDzQAmDPDqCs");
	this.shape.setTransform(56.6,74.9);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#93AD40").s().p("AhFAUIBHggIBEggIgHBZg");
	this.shape_1.setTransform(28,151.2);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-1.5,-1.5,116.2,157.2);


(lib.arrowBlue = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.shape = new cjs.Shape();
	this.shape.graphics.f().s("#3CBACC").ss(3,1,0,3).p("A4/j6QJOE0HEB5QHEB5GVhLQGVhMFwijQFuilChhK");
	this.shape.setTransform(167.1,29.8);

	this.shape_1 = new cjs.Shape();
	this.shape_1.graphics.f("#3DBACC").s().p("Ag5gnIB/AQIhGAeIhFAhg");
	this.shape_1.setTransform(7,4);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.shape_1},{t:this.shape}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(0,0,328.6,56.6);


(lib.gain = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.instance = new lib.dollarGrey("synched",0);
	this.instance.parent = this;
	this.instance.setTransform(0.1,-2.3,1,1,0,0,0,12.1,6.2);

	this.instance_1 = new lib.dollarGrey("synched",0);
	this.instance_1.parent = this;
	this.instance_1.setTransform(0.1,0.1,1,1,0,0,0,12.1,6.2);

	this.instance_2 = new lib.dollarGrey("synched",0);
	this.instance_2.parent = this;
	this.instance_2.setTransform(0.1,2.5,1,1,0,0,0,12.1,6.2);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.instance_2},{t:this.instance_1},{t:this.instance}]}).wait(1));

}).prototype = getMCSymbolPrototype(lib.gain, new cjs.Rectangle(-12,-8.5,24.1,17.1), null);


(lib.dollarsGreyInChariot = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.instance = new lib.dollarGrey("synched",0);
	this.instance.parent = this;
	this.instance.setTransform(9.4,-0.7,0.675,0.675,0,0,0,12.1,6.2);

	this.instance_1 = new lib.dollarGrey("synched",0);
	this.instance_1.parent = this;
	this.instance_1.setTransform(2.9,-4.4,0.675,0.675,0,0,0,12.1,6.2);

	this.instance_2 = new lib.dollarGrey("synched",0);
	this.instance_2.parent = this;
	this.instance_2.setTransform(-2.8,4.6,0.675,0.675,0,0,0,12.1,6.2);

	this.instance_3 = new lib.dollarGrey("synched",0);
	this.instance_3.parent = this;
	this.instance_3.setTransform(-9.3,0.8,0.675,0.675,0,0,0,12.1,6.2);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.instance_3},{t:this.instance_2},{t:this.instance_1},{t:this.instance}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-17.5,-8.6,35,17.3);


(lib.dollarsColorsInChariot = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 1
	this.instance = new lib.dollarBlue("synched",0);
	this.instance.parent = this;
	this.instance.setTransform(9.4,-0.7,0.675,0.675,0,0,0,12.1,6.2);

	this.instance_1 = new lib.dollarOrange("synched",0);
	this.instance_1.parent = this;
	this.instance_1.setTransform(2.9,-4.4,0.675,0.675,0,0,0,12.1,6.2);

	this.instance_2 = new lib.dollarRed("synched",0);
	this.instance_2.parent = this;
	this.instance_2.setTransform(-2.8,4.6,0.675,0.675,0,0,0,12.1,6.2);

	this.instance_3 = new lib.dollarGreen("synched",0);
	this.instance_3.parent = this;
	this.instance_3.setTransform(-9.3,0.8,0.675,0.675,0,0,0,12.1,6.2);

	this.timeline.addTween(cjs.Tween.get({}).to({state:[{t:this.instance_3},{t:this.instance_2},{t:this.instance_1},{t:this.instance}]}).wait(1));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(-17.5,-8.6,35,17.3);


(lib.cart = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{});

	// Calque 2
	this.bubble = new lib.bubbleBlack();
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
(lib.public_good_simulation = function(mode,startPosition,loop) {
	this.initialize(mode,startPosition,loop,{init:0,start:35,send:55,multiply:151,finish:187,results:257});

	// timeline functions:
	this.frame_35 = function() {
		/*
		 Process
		 -------
		 Find if canvas in HTML shell page has the following data-attributes:
		 - `data-min`
		 - `data-max`
		 - `data-currency`
		 - `data-multipler`
		 
		 Use them as attributes in the animation if found.
		 Use default attributes if not.
		 
		 Assumes there is only on canvas in the page.
		 */
		 
		var self = this;
		var min = 0;
		var max = 12000;
		var currency = '€';
		var multiplier = 1.6;
		var resultMoney = 0;
		var NUM_PLAYERS = 4;
		var locale = 'ko';
		
		if (document) {
			var canvas = document.getElementsByTagName('canvas')[0];
			if (canvas) {
				min = +canvas.getAttribute('data-min') || min;
				max = +canvas.getAttribute('data-max') || max;
				currency = canvas.getAttribute('data-currency')|| currency;
				multiplier = +canvas.getAttribute('data-multiplier') || multiplier;
				locale = canvas.getAttribute('data-locale') || locale;
			}
		}
			
		function setMoneyText(money) {
			return currency + money.toString();
		}
		
		function getRandomInt(min, max) {
			return Math.floor(Math.random() * (max - min)) + min;
		}
		
		function Player(startAmount, bubbleRef) {
			this.startAmount = startAmount;
			this.currentAmount = startAmount;
			this.givingAmount = 0;
			this.bubble = bubbleRef;
			this.bubble.label.text = currency + max;
		};
		
		if (locale === 'ko') {
			this.bubble1.label.font = "16px 'Gotham Medium'";
			this.bubble2.label.font = "16px 'Gotham Medium'";
			this.bubble3.label.font = "16px 'Gotham Medium'";
			this.bubble4.label.font = "16px 'Gotham Medium'";
			this.cart.bubble.label.font = "16px 'Gotham Medium'";
		}
		
		Player.prototype.giveMoney = function (amount) {
			if (amount <= max) {
				this.currentAmount = max - amount;
				
				var displayedAmount = (
					this.currentAmount % 1 === 0 ? this.currentAmount.toString() : this.currentAmount.toFixed(2).toString()
				);
				
				this.speak(currency + displayedAmount);
				this.givingAmount = amount;
			}
		};
		
		Player.prototype.receiveMoney = function (amount) {
			this.currentAmount += amount;
			this.speak(currency + this.currentAmount.toFixed(2).toString());
		};
		
		Player.prototype.speak = function (text) {
			this.bubble.label.text = text;
		};
		
		var p1 = new Player(max, this.bubble1);
		var p2 = new Player(max, this.bubble2);
		var p3 = new Player(max, this.bubble3);
		var p4 = new Player(max, this.bubble4);
		
		var moneyFromGroup = function () {
			return p1.givingAmount + p2.givingAmount + p3.givingAmount + p4.givingAmount;
		}
		
		this.bubbleMultiplier.label.text = '×' + multiplier;
		
		window.PG = (function () {
			var players = [p1, p2, p3, p4];
			
			var giveMoney = function (playerIndex, amount) {
				players[playerIndex].giveMoney(+amount);
				self.cart.bubble.alpha = 1;
				self.cart.bubble.label.text = locale === 'ko' ? currency + moneyFromGroup().toString() : currency + moneyFromGroup().toFixed(2).toString();
			};
			
			var multiply = function () {
				multipliedAmount = moneyFromGroup() * multiplier;
				self.cart.bubble.label.text = currency + multipliedAmount.toFixed(2).toString();
			};
		
			var send = function () {
				resultMoney = (+moneyFromGroup() * +multiplier) / +NUM_PLAYERS;
				
				setTimeout(function () {
					self.cart.bubble.alpha = 1;
					self.cart.bubble.label.text = currency + moneyFromGroup().toFixed(2).toString();
				}, 2000);
				
				/* setTimeout(function () {
					var multipliedAmount = moneyFromGroup() * multiplier;
					self.cart.bubble.label.text = currency + multipliedAmount.toString();
				}, 4000);*/
				
				
				self.gotoAndPlay('send');
			};
			
			var receive = function () {
				p1.receiveMoney(+resultMoney);
				p2.receiveMoney(+resultMoney);
				p3.receiveMoney(+resultMoney);
				p4.receiveMoney(+resultMoney);
				self.cart.bubble.label.text = currency + '0';
			}
			
			return {
				giveMoney: giveMoney,
				send: send,
				multiply: multiply,
				receive: receive
			}
		})();
	}
	this.frame_54 = function() {
		this.stop();
	}
	this.frame_146 = function() {
		this.stop();
		this.gotoAndPlay('multiply');
		window.PG.multiply();
	}
	this.frame_186 = function() {
		this.stop();
		this.gotoAndPlay('finish');
	}
	this.frame_236 = function() {
		this.stop();
		this.gotoAndPlay('results');
	}
	this.frame_257 = function() {
		window.PG.receive();
	}
	this.frame_499 = function() {
		this.gotoAndPlay('start');
	}

	// actions tween:
	this.timeline.addTween(cjs.Tween.get(this).wait(35).call(this.frame_35).wait(19).call(this.frame_54).wait(92).call(this.frame_146).wait(40).call(this.frame_186).wait(50).call(this.frame_236).wait(21).call(this.frame_257).wait(242).call(this.frame_499).wait(1));

	// bubble multiplier
	this.bubbleMultiplier = new lib.multiplier();
	this.bubbleMultiplier.parent = this;
	this.bubbleMultiplier.setTransform(274.1,155,0.141,0.161,0,0,32.7);
	this.bubbleMultiplier.alpha = 0;
	this.bubbleMultiplier._off = true;

	this.timeline.addTween(cjs.Tween.get(this.bubbleMultiplier).wait(35).to({_off:false},0).wait(116).to({scaleX:0.88,scaleY:1,skewY:32.6,y:113.4,alpha:1},4,cjs.Ease.get(1)).to({scaleX:0.88,y:101.7},28).to({scaleX:0.88,skewY:32.7,y:99,alpha:0},3).to({_off:true},1).wait(313));

	// gain 4
	this.instance = new lib.gain("synched",0);
	this.instance.parent = this;
	this.instance.setTransform(560.5,385.1,1,1,0,0,0,12.1,6.2);
	this.instance.alpha = 0;
	this.instance._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance).wait(257).to({_off:false},0).to({alpha:1},9,cjs.Ease.get(1)).wait(228).to({startPosition:0},0).to({alpha:0},5,cjs.Ease.get(1)).wait(1));

	// gain 3
	this.instance_1 = new lib.gain("synched",0);
	this.instance_1.parent = this;
	this.instance_1.setTransform(483.2,337.4,1,1,0,0,0,12.1,6.2);
	this.instance_1.alpha = 0;
	this.instance_1._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_1).wait(257).to({_off:false},0).to({alpha:1},9,cjs.Ease.get(1)).wait(228).to({startPosition:0},0).to({alpha:0},5,cjs.Ease.get(1)).wait(1));

	// gain 2
	this.instance_2 = new lib.gain("synched",0);
	this.instance_2.parent = this;
	this.instance_2.setTransform(401.8,289.7,1,1,0,0,0,12.1,6.2);
	this.instance_2.alpha = 0;
	this.instance_2._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_2).wait(257).to({_off:false},0).to({alpha:1},9,cjs.Ease.get(1)).wait(228).to({startPosition:0},0).to({alpha:0},5,cjs.Ease.get(1)).wait(1));

	// gain 1
	this.instance_3 = new lib.gain();
	this.instance_3.parent = this;
	this.instance_3.setTransform(181.7,149.5);
	this.instance_3.alpha = 0;
	this.instance_3._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_3).wait(257).to({_off:false},0).to({alpha:1},9,cjs.Ease.get(1)).wait(228).to({alpha:0},5,cjs.Ease.get(1)).wait(1));

	// bubble 4
	this.bubble4 = new lib.bubbleRed();
	this.bubble4.parent = this;
	this.bubble4.setTransform(547.6,321.7,0.099,0.084,0,0,32,38.3,41.9);
	this.bubble4._off = true;

	this.timeline.addTween(cjs.Tween.get(this.bubble4).wait(50).to({_off:false},0).to({regY:41.8,scaleX:0.79,scaleY:0.67,x:539.6,y:305.7},4,cjs.Ease.get(1)).wait(1).to({regY:41.9,scaleX:0.1,scaleY:0.08,x:547.6,y:321.7,alpha:0},3,cjs.Ease.get(1)).wait(199).to({regY:41.8,scaleX:0.79,scaleY:0.67,x:539.6,y:305.7,alpha:1},3,cjs.Ease.get(1)).wait(234).to({regY:41.9,scaleX:0.1,scaleY:0.08,x:547.6,y:321.7},5,cjs.Ease.get(1)).wait(1));

	// bubble 3
	this.bubble3 = new lib.bubbleBlue();
	this.bubble3.parent = this;
	this.bubble3.setTransform(476.6,278.6,0.167,0.141,0,0,32,38.2,42);
	this.bubble3._off = true;

	this.timeline.addTween(cjs.Tween.get(this.bubble3).wait(50).to({_off:false},0).to({regX:38.3,regY:41.8,scaleX:0.79,scaleY:0.67,x:460.6,y:254.5},4,cjs.Ease.get(1)).wait(1).to({regX:38.2,regY:42,scaleX:0.17,scaleY:0.14,x:476.6,y:278.6,alpha:0},3,cjs.Ease.get(1)).wait(199).to({regX:38.3,regY:41.8,scaleX:0.79,scaleY:0.67,x:460.6,y:254.5,alpha:1},3,cjs.Ease.get(1)).wait(234).to({regX:38.2,regY:42,scaleX:0.17,scaleY:0.14,x:476.6,y:278.6},5,cjs.Ease.get(1)).wait(1));

	// bubble 2
	this.bubble2 = new lib.bubbleOrange();
	this.bubble2.parent = this;
	this.bubble2.setTransform(400.1,231.9,0.147,0.124,0,0,32,38.2,42.1);
	this.bubble2._off = true;

	this.timeline.addTween(cjs.Tween.get(this.bubble2).wait(50).to({_off:false},0).to({regX:38.3,regY:41.8,scaleX:0.79,scaleY:0.67,x:376.2,y:199.8},4,cjs.Ease.get(1)).wait(1).to({regX:38.2,regY:42.1,scaleX:0.15,scaleY:0.12,x:400.1,y:231.9,alpha:0},3,cjs.Ease.get(1)).wait(199).to({regX:38.3,regY:41.8,scaleX:0.79,scaleY:0.67,x:376.2,y:199.8,alpha:1},3,cjs.Ease.get(1)).wait(234).to({regX:38.2,regY:42.1,scaleX:0.15,scaleY:0.12,x:400.1,y:231.9},5,cjs.Ease.get(1)).wait(1));

	// bubble 1
	this.bubble1 = new lib.bubbleGreen();
	this.bubble1.parent = this;
	this.bubble1.setTransform(193.4,104.3,0.139,0.118,0,0,32,38.2,42);
	this.bubble1._off = true;

	this.timeline.addTween(cjs.Tween.get(this.bubble1).wait(50).to({_off:false},0).to({regX:38.3,regY:41.8,scaleX:0.79,scaleY:0.67,x:169.4,y:80.2},4,cjs.Ease.get(1)).wait(1).to({regX:38.2,regY:42,scaleX:0.14,scaleY:0.12,x:193.4,y:104.3,alpha:0},3,cjs.Ease.get(1)).wait(199).to({regX:38.3,regY:41.8,scaleX:0.79,scaleY:0.67,x:169.4,y:80.2,alpha:1},3,cjs.Ease.get(1)).wait(234).to({regX:38.2,regY:42,scaleX:0.14,scaleY:0.12,x:193.4,y:104.3},5,cjs.Ease.get(1)).wait(1));

	// mask (mask)
	var mask = new cjs.Shape();
	mask._off = true;
	var mask_graphics_0 = new cjs.Graphics().p("EgF2AzFMABkgs/IoIloMAAAgziIRVAAIAAAnIHgAAMAAABlig");
	var mask_graphics_494 = new cjs.Graphics().p("EgF2AzFMABkgs/IoIloMAAAgziIRVAAIAAAnIHgAAMAAABlig");

	this.timeline.addTween(cjs.Tween.get(mask).to({graphics:mask_graphics_0,x:301.5,y:210}).wait(494).to({graphics:mask_graphics_494,x:301.5,y:210}).wait(6));

	// factory front
	this.instance_4 = new lib.factory();
	this.instance_4.parent = this;
	this.instance_4.setTransform(261.7,-54.2,1,1,0,0,0,-34.8,34.6);

	var maskedShapeInstanceList = [this.instance_4];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance_4).to({y:249.8},9,cjs.Ease.get(1)).wait(491));

	// chariot money grey copy 4
	this.instance_5 = new lib.dollarsGreyInChariot("synched",0);
	this.instance_5.parent = this;
	this.instance_5.setTransform(287.8,256.2);
	this.instance_5._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_5).wait(191).to({_off:false},0).to({x:487.8,y:165.8},45,cjs.Ease.get(1)).wait(21).to({startPosition:0},0).to({alpha:0},9,cjs.Ease.get(1)).wait(228).to({startPosition:0},0).wait(6));

	// chariot money grey copy 3
	this.instance_6 = new lib.dollarsGreyInChariot("synched",0);
	this.instance_6.parent = this;
	this.instance_6.setTransform(287.8,257.8);
	this.instance_6._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_6).wait(191).to({_off:false},0).to({x:487.8,y:168.2},45,cjs.Ease.get(1)).wait(21).to({startPosition:0},0).to({alpha:0},9,cjs.Ease.get(1)).wait(228).to({startPosition:0},0).wait(6));

	// chariot money grey copy 2
	this.instance_7 = new lib.dollarsGreyInChariot("synched",0);
	this.instance_7.parent = this;
	this.instance_7.setTransform(287.8,260.2);
	this.instance_7._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_7).wait(191).to({_off:false},0).to({x:487.8,y:170.6},45,cjs.Ease.get(1)).wait(21).to({startPosition:0},0).to({alpha:0},9,cjs.Ease.get(1)).wait(228).to({startPosition:0},0).wait(6));

	// chariot money grey copy
	this.instance_8 = new lib.dollarsGreyInChariot("synched",0);
	this.instance_8.parent = this;
	this.instance_8.setTransform(287.8,262.6);
	this.instance_8._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_8).wait(191).to({_off:false},0).to({x:487.8,y:173},45,cjs.Ease.get(1)).wait(21).to({startPosition:0},0).to({alpha:0},9,cjs.Ease.get(1)).wait(228).to({startPosition:0},0).wait(6));

	// chariot money colors
	this.instance_9 = new lib.dollarsColorsInChariot("synched",0);
	this.instance_9.parent = this;
	this.instance_9.setTransform(112.6,340.2);
	this.instance_9.alpha = 0;
	this.instance_9._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_9).wait(72).to({_off:false},0).to({alpha:1},5,cjs.Ease.get(1)).wait(19).to({startPosition:0},0).to({x:288.6,y:261.8},50,cjs.Ease.get(1)).wait(354));

	// arrow 4
	this.instance_10 = new lib.arrowRed("synched",0);
	this.instance_10.parent = this;
	this.instance_10.setTransform(325.9,410.4,1,1,0,0,0,210.6,48.2);
	this.instance_10.alpha = 0;
	this.instance_10._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_10).wait(59).to({_off:false},0).to({alpha:1},9,cjs.Ease.get(1)).wait(18).to({startPosition:0},0).to({alpha:0},5,cjs.Ease.get(1)).wait(409));

	// arrow 3
	this.instance_11 = new lib.arrowBlue("synched",0);
	this.instance_11.parent = this;
	this.instance_11.setTransform(294,384.3,1,1,0,0,0,164.2,28.3);
	this.instance_11.alpha = 0;
	this.instance_11._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_11).wait(59).to({_off:false},0).to({alpha:1},9,cjs.Ease.get(1)).wait(18).to({startPosition:0},0).to({alpha:0},5,cjs.Ease.get(1)).wait(409));

	// arrow 2
	this.instance_12 = new lib.arrowOrange("synched",0);
	this.instance_12.parent = this;
	this.instance_12.setTransform(260.1,341.7,1,1,0,0,0,116.2,28.3);
	this.instance_12.alpha = 0;
	this.instance_12._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_12).wait(59).to({_off:false},0).to({alpha:1},9,cjs.Ease.get(1)).wait(18).to({startPosition:0},0).to({alpha:0},5,cjs.Ease.get(1)).wait(409));

	// arrow 1
	this.instance_13 = new lib.arrowGreen("synched",0);
	this.instance_13.parent = this;
	this.instance_13.setTransform(110,254.4,1,1,0,0,0,56.6,77.1);
	this.instance_13.alpha = 0;
	this.instance_13._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_13).wait(59).to({_off:false},0).to({alpha:1},9,cjs.Ease.get(1)).wait(18).to({startPosition:0},0).to({alpha:0},5,cjs.Ease.get(1)).wait(409));

	// chariot
	this.cart = new lib.cart();
	this.cart.parent = this;
	this.cart.setTransform(113,342.3,0.817,0.817,0,0,0,30.9,17.8);
	this.cart.alpha = 0;
	this.cart._off = true;

	this.timeline.addTween(cjs.Tween.get(this.cart).wait(35).to({_off:false},0).to({alpha:1},4,cjs.Ease.get(1)).wait(57).to({x:289,y:263.9},50,cjs.Ease.get(1)).wait(45).to({x:488.2,y:175.1},45,cjs.Ease.get(1)).wait(258).to({alpha:0},5,cjs.Ease.get(1)).wait(1));

	// d1-10 copy 3
	this.instance_14 = new lib.dollarRed("synched",0);
	this.instance_14.parent = this;
	this.instance_14.setTransform(548.5,-32.7,1,1,0,0,0,12.1,6.2);
	this.instance_14._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_14).wait(32).to({_off:false},0).to({y:383.3},3).wait(459).to({startPosition:0},0).wait(6));

	// d1-9 copy 3
	this.instance_15 = new lib.dollarRed("synched",0);
	this.instance_15.parent = this;
	this.instance_15.setTransform(548.5,-30.8,1,1,0,0,0,12.1,6.2);
	this.instance_15._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_15).wait(31).to({_off:false},0).to({y:385.2},3).wait(460).to({startPosition:0},0).wait(6));

	// d1-8 copy 3
	this.instance_16 = new lib.dollarRed("synched",0);
	this.instance_16.parent = this;
	this.instance_16.setTransform(548.5,-28.8,1,1,0,0,0,12.1,6.2);
	this.instance_16._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_16).wait(30).to({_off:false},0).to({y:387.2},3).wait(461).to({startPosition:0},0).wait(6));

	// d1-7 copy 3
	this.instance_17 = new lib.dollarRed("synched",0);
	this.instance_17.parent = this;
	this.instance_17.setTransform(548.5,-26.9,1,1,0,0,0,12.1,6.2);
	this.instance_17._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_17).wait(29).to({_off:false},0).to({y:389.1},3).wait(462).to({startPosition:0},0).wait(6));

	// d1-6 copy 3
	this.instance_18 = new lib.dollarRed("synched",0);
	this.instance_18.parent = this;
	this.instance_18.setTransform(548.5,-24.9,1,1,0,0,0,12.1,6.2);
	this.instance_18._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_18).wait(28).to({_off:false},0).to({y:391.1},3).wait(463).to({startPosition:0},0).wait(6));

	// d1-5 copy 3
	this.instance_19 = new lib.dollarRed("synched",0);
	this.instance_19.parent = this;
	this.instance_19.setTransform(548.5,-23,1,1,0,0,0,12.1,6.2);
	this.instance_19._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_19).wait(27).to({_off:false},0).to({y:393},3).wait(464).to({startPosition:0},0).wait(6));

	// d1-4 copy 3
	this.instance_20 = new lib.dollarRed("synched",0);
	this.instance_20.parent = this;
	this.instance_20.setTransform(548.5,-21,1,1,0,0,0,12.1,6.2);
	this.instance_20._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_20).wait(26).to({_off:false},0).to({y:395},3).wait(465).to({startPosition:0},0).wait(6));

	// d1-3 copy 3
	this.instance_21 = new lib.dollarRed("synched",0);
	this.instance_21.parent = this;
	this.instance_21.setTransform(548.5,-19.1,1,1,0,0,0,12.1,6.2);
	this.instance_21._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_21).wait(25).to({_off:false},0).to({y:396.9},3).wait(466).to({startPosition:0},0).wait(6));

	// d1-2 copy 3
	this.instance_22 = new lib.dollarRed("synched",0);
	this.instance_22.parent = this;
	this.instance_22.setTransform(548.5,-17.1,1,1,0,0,0,12.1,6.2);
	this.instance_22._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_22).wait(24).to({_off:false},0).to({y:398.9},3).wait(467).to({startPosition:0},0).wait(6));

	// d1-1 copy 3
	this.instance_23 = new lib.dollarRed("synched",0);
	this.instance_23.parent = this;
	this.instance_23.setTransform(548.5,-15.2,1,1,0,0,0,12.1,6.2);
	this.instance_23._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_23).wait(23).to({_off:false},0).to({y:400.8},3).wait(468).to({startPosition:0},0).wait(6));

	// d1-10 copy 2
	this.instance_24 = new lib.dollarBlue("synched",0);
	this.instance_24.parent = this;
	this.instance_24.setTransform(471.2,-32.2,1,1,0,0,0,12.1,6.2);
	this.instance_24._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_24).wait(30).to({_off:false},0).to({y:335.8},3,cjs.Ease.get(1)).wait(461).to({startPosition:0},0).wait(6));

	// d1-9 copy 2
	this.instance_25 = new lib.dollarBlue("synched",0);
	this.instance_25.parent = this;
	this.instance_25.setTransform(471.2,-30.2,1,1,0,0,0,12.1,6.2);
	this.instance_25._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_25).wait(29).to({_off:false},0).to({y:337.8},3,cjs.Ease.get(1)).wait(462).to({startPosition:0},0).wait(6));

	// d1-8 copy 2
	this.instance_26 = new lib.dollarBlue("synched",0);
	this.instance_26.parent = this;
	this.instance_26.setTransform(471.2,-28.3,1,1,0,0,0,12.1,6.2);
	this.instance_26._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_26).wait(28).to({_off:false},0).to({y:339.7},3,cjs.Ease.get(1)).wait(463).to({startPosition:0},0).wait(6));

	// d1-7 copy 2
	this.instance_27 = new lib.dollarBlue("synched",0);
	this.instance_27.parent = this;
	this.instance_27.setTransform(471.2,-26.3,1,1,0,0,0,12.1,6.2);
	this.instance_27._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_27).wait(27).to({_off:false},0).to({y:341.7},3,cjs.Ease.get(1)).wait(464).to({startPosition:0},0).wait(6));

	// d1-6 copy 2
	this.instance_28 = new lib.dollarBlue("synched",0);
	this.instance_28.parent = this;
	this.instance_28.setTransform(471.2,-24.4,1,1,0,0,0,12.1,6.2);
	this.instance_28._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_28).wait(26).to({_off:false},0).to({y:343.6},3,cjs.Ease.get(1)).wait(465).to({startPosition:0},0).wait(6));

	// d1-5 copy 2
	this.instance_29 = new lib.dollarBlue("synched",0);
	this.instance_29.parent = this;
	this.instance_29.setTransform(471.2,-22.4,1,1,0,0,0,12.1,6.2);
	this.instance_29._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_29).wait(25).to({_off:false},0).to({y:345.6},3,cjs.Ease.get(1)).wait(466).to({startPosition:0},0).wait(6));

	// d1-4 copy 2
	this.instance_30 = new lib.dollarBlue("synched",0);
	this.instance_30.parent = this;
	this.instance_30.setTransform(471.2,-20.5,1,1,0,0,0,12.1,6.2);
	this.instance_30._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_30).wait(24).to({_off:false},0).to({y:347.5},3,cjs.Ease.get(1)).wait(467).to({startPosition:0},0).wait(6));

	// d1-3 copy 2
	this.instance_31 = new lib.dollarBlue("synched",0);
	this.instance_31.parent = this;
	this.instance_31.setTransform(471.2,-18.5,1,1,0,0,0,12.1,6.2);
	this.instance_31._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_31).wait(23).to({_off:false},0).to({y:349.5},3,cjs.Ease.get(1)).wait(468).to({startPosition:0},0).wait(6));

	// d1-2 copy 2
	this.instance_32 = new lib.dollarBlue("synched",0);
	this.instance_32.parent = this;
	this.instance_32.setTransform(471.2,-16.6,1,1,0,0,0,12.1,6.2);
	this.instance_32._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_32).wait(22).to({_off:false},0).to({y:351.4},3,cjs.Ease.get(1)).wait(469).to({startPosition:0},0).wait(6));

	// d1-1 copy 2
	this.instance_33 = new lib.dollarBlue("synched",0);
	this.instance_33.parent = this;
	this.instance_33.setTransform(471.2,-14.6,1,1,0,0,0,12.1,6.2);
	this.instance_33._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_33).wait(21).to({_off:false},0).to({y:353.4},3,cjs.Ease.get(1)).wait(470).to({startPosition:0},0).wait(6));

	// d1-10 copy
	this.instance_34 = new lib.dollarOrange("synched",0);
	this.instance_34.parent = this;
	this.instance_34.setTransform(389.8,288.1,1,1,0,0,0,12.1,6.2);
	this.instance_34.alpha = 0;
	this.instance_34._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_34).wait(28).to({_off:false},0).to({alpha:1},3,cjs.Ease.get(1)).wait(463).to({startPosition:0},0).wait(6));

	// d1-9 copy
	this.instance_35 = new lib.dollarOrange("synched",0);
	this.instance_35.parent = this;
	this.instance_35.setTransform(389.8,290,1,1,0,0,0,12.1,6.2);
	this.instance_35.alpha = 0;
	this.instance_35._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_35).wait(27).to({_off:false},0).to({alpha:1},3,cjs.Ease.get(1)).wait(464).to({startPosition:0},0).wait(6));

	// d1-8 copy
	this.instance_36 = new lib.dollarOrange("synched",0);
	this.instance_36.parent = this;
	this.instance_36.setTransform(389.8,292,1,1,0,0,0,12.1,6.2);
	this.instance_36.alpha = 0;
	this.instance_36._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_36).wait(26).to({_off:false},0).to({alpha:1},3,cjs.Ease.get(1)).wait(465).to({startPosition:0},0).wait(6));

	// d1-7 copy
	this.instance_37 = new lib.dollarOrange("synched",0);
	this.instance_37.parent = this;
	this.instance_37.setTransform(389.8,293.9,1,1,0,0,0,12.1,6.2);
	this.instance_37.alpha = 0;
	this.instance_37._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_37).wait(25).to({_off:false},0).to({alpha:1},3,cjs.Ease.get(1)).wait(466).to({startPosition:0},0).wait(6));

	// d1-6 copy
	this.instance_38 = new lib.dollarOrange("synched",0);
	this.instance_38.parent = this;
	this.instance_38.setTransform(389.8,295.9,1,1,0,0,0,12.1,6.2);
	this.instance_38.alpha = 0;
	this.instance_38._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_38).wait(24).to({_off:false},0).to({alpha:1},3,cjs.Ease.get(1)).wait(467).to({startPosition:0},0).wait(6));

	// d1-5 copy
	this.instance_39 = new lib.dollarOrange("synched",0);
	this.instance_39.parent = this;
	this.instance_39.setTransform(389.8,297.8,1,1,0,0,0,12.1,6.2);
	this.instance_39.alpha = 0;
	this.instance_39._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_39).wait(23).to({_off:false},0).to({alpha:1},3,cjs.Ease.get(1)).wait(468).to({startPosition:0},0).wait(6));

	// d1-4 copy
	this.instance_40 = new lib.dollarOrange("synched",0);
	this.instance_40.parent = this;
	this.instance_40.setTransform(389.8,299.8,1,1,0,0,0,12.1,6.2);
	this.instance_40.alpha = 0;
	this.instance_40._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_40).wait(22).to({_off:false},0).to({alpha:1},3,cjs.Ease.get(1)).wait(469).to({startPosition:0},0).wait(6));

	// d1-3 copy
	this.instance_41 = new lib.dollarOrange("synched",0);
	this.instance_41.parent = this;
	this.instance_41.setTransform(389.8,301.7,1,1,0,0,0,12.1,6.2);
	this.instance_41.alpha = 0;
	this.instance_41._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_41).wait(21).to({_off:false},0).to({alpha:1},3,cjs.Ease.get(1)).wait(470).to({startPosition:0},0).wait(6));

	// d1-2 copy
	this.instance_42 = new lib.dollarOrange("synched",0);
	this.instance_42.parent = this;
	this.instance_42.setTransform(389.8,303.7,1,1,0,0,0,12.1,6.2);
	this.instance_42.alpha = 0;
	this.instance_42._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_42).wait(20).to({_off:false},0).to({alpha:1},3,cjs.Ease.get(1)).wait(471).to({startPosition:0},0).wait(6));

	// d1-1 copy
	this.instance_43 = new lib.dollarOrange("synched",0);
	this.instance_43.parent = this;
	this.instance_43.setTransform(389.8,305.6,1,1,0,0,0,12.1,6.2);
	this.instance_43.alpha = 0;
	this.instance_43._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_43).wait(19).to({_off:false},0).to({alpha:1},3,cjs.Ease.get(1)).wait(472).to({startPosition:0},0).wait(6));

	// d1-10
	this.instance_44 = new lib.dollarGreen("synched",0);
	this.instance_44.parent = this;
	this.instance_44.setTransform(181.8,-29.6,1,1,0,0,0,12.1,6.2);
	this.instance_44._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_44).wait(26).to({_off:false},0).to({y:154.4},3,cjs.Ease.get(1)).wait(465).to({startPosition:0},0).wait(6));

	// d1-9
	this.instance_45 = new lib.dollarGreen("synched",0);
	this.instance_45.parent = this;
	this.instance_45.setTransform(181.8,-27.7,1,1,0,0,0,12.1,6.2);
	this.instance_45._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_45).wait(25).to({_off:false},0).to({y:156.3},3,cjs.Ease.get(1)).wait(466).to({startPosition:0},0).wait(6));

	// d1-8
	this.instance_46 = new lib.dollarGreen("synched",0);
	this.instance_46.parent = this;
	this.instance_46.setTransform(181.8,-25.7,1,1,0,0,0,12.1,6.2);
	this.instance_46._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_46).wait(24).to({_off:false},0).to({y:158.3},3,cjs.Ease.get(1)).wait(467).to({startPosition:0},0).wait(6));

	// d1-7
	this.instance_47 = new lib.dollarGreen("synched",0);
	this.instance_47.parent = this;
	this.instance_47.setTransform(181.8,-23.8,1,1,0,0,0,12.1,6.2);
	this.instance_47._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_47).wait(23).to({_off:false},0).to({y:160.2},3,cjs.Ease.get(1)).wait(468).to({startPosition:0},0).wait(6));

	// d1-6
	this.instance_48 = new lib.dollarGreen("synched",0);
	this.instance_48.parent = this;
	this.instance_48.setTransform(181.8,-21.8,1,1,0,0,0,12.1,6.2);
	this.instance_48._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_48).wait(22).to({_off:false},0).to({y:162.2},3,cjs.Ease.get(1)).wait(469).to({startPosition:0},0).wait(6));

	// d1-5
	this.instance_49 = new lib.dollarGreen("synched",0);
	this.instance_49.parent = this;
	this.instance_49.setTransform(181.8,-19.9,1,1,0,0,0,12.1,6.2);
	this.instance_49._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_49).wait(21).to({_off:false},0).to({y:164.1},3,cjs.Ease.get(1)).wait(470).to({startPosition:0},0).wait(6));

	// d1-4
	this.instance_50 = new lib.dollarGreen("synched",0);
	this.instance_50.parent = this;
	this.instance_50.setTransform(181.8,-17.9,1,1,0,0,0,12.1,6.2);
	this.instance_50._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_50).wait(20).to({_off:false},0).to({y:166.1},3,cjs.Ease.get(1)).wait(471).to({startPosition:0},0).wait(6));

	// d1-3
	this.instance_51 = new lib.dollarGreen("synched",0);
	this.instance_51.parent = this;
	this.instance_51.setTransform(181.8,-16,1,1,0,0,0,12.1,6.2);
	this.instance_51._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_51).wait(19).to({_off:false},0).to({y:168},3,cjs.Ease.get(1)).wait(472).to({startPosition:0},0).wait(6));

	// d1-2
	this.instance_52 = new lib.dollarGreen("synched",0);
	this.instance_52.parent = this;
	this.instance_52.setTransform(181.8,-14,1,1,0,0,0,12.1,6.2);
	this.instance_52._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_52).wait(18).to({_off:false},0).to({y:170},3,cjs.Ease.get(1)).wait(473).to({startPosition:0},0).wait(6));

	// d1-1
	this.instance_53 = new lib.dollarGreen("synched",0);
	this.instance_53.parent = this;
	this.instance_53.setTransform(181.8,-12.1,1,1,0,0,0,12.1,6.2);
	this.instance_53._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_53).wait(17).to({_off:false},0).to({y:171.9},3,cjs.Ease.get(1)).wait(474).to({startPosition:0},0).wait(6));

	// char 4
	this.instance_54 = new lib.character("synched",0);
	this.instance_54.parent = this;
	this.instance_54.setTransform(565.7,-32.2,1,1,0,0,0,5.2,27.4);
	this.instance_54._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_54).wait(17).to({_off:false},0).to({y:367.8},3,cjs.Ease.get(1)).wait(474).to({startPosition:0},0).wait(6));

	// char 3
	this.instance_55 = new lib.character("synched",0);
	this.instance_55.parent = this;
	this.instance_55.setTransform(488.4,-31.9,1,1,0,0,0,5.2,27.4);
	this.instance_55._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_55).wait(16).to({_off:false},0).to({y:320.1},3,cjs.Ease.get(1)).wait(475).to({startPosition:0},0).wait(6));

	// char 2
	this.instance_56 = new lib.character("synched",0);
	this.instance_56.parent = this;
	this.instance_56.setTransform(409.8,-32.9,1,1,0,0,0,5.2,27.4);
	this.instance_56._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_56).wait(15).to({_off:false},0).to({y:271.1},3,cjs.Ease.get(1)).wait(476).to({startPosition:0},0).wait(6));

	// char 1
	this.instance_57 = new lib.character("synched",0);
	this.instance_57.parent = this;
	this.instance_57.setTransform(201.2,-28.4,1,1,0,0,0,5.2,27.4);
	this.instance_57._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_57).wait(14).to({_off:false},0).to({y:139.6},3,cjs.Ease.get(1)).wait(477).to({startPosition:0},0).wait(6));

	// conveyor belt
	this.instance_58 = new lib.conveyor("synched",0);
	this.instance_58.parent = this;
	this.instance_58.setTransform(267,292,1,1,0,0,180);
	this.instance_58.alpha = 0;
	this.instance_58._off = true;

	this.timeline.addTween(cjs.Tween.get(this.instance_58).wait(9).to({_off:false},0).to({alpha:1},5,cjs.Ease.get(1)).wait(480).to({startPosition:0},0).wait(6));

	// mask (mask)
	var mask_1 = new cjs.Shape();
	mask_1._off = true;
	var mask_1_graphics_0 = new cjs.Graphics().p("EAJIBPDMAAAieFIMSAAMAAACeFg");
	var mask_1_graphics_494 = new cjs.Graphics().p("EAJIBPDMAAAieFIMSAAMAAACeFg");

	this.timeline.addTween(cjs.Tween.get(mask_1).to({graphics:mask_1_graphics_0,x:137,y:220.2}).wait(494).to({graphics:mask_1_graphics_494,x:137,y:220.2}).wait(6));

	// factory back
	this.instance_59 = new lib.factory();
	this.instance_59.parent = this;
	this.instance_59.setTransform(261.7,-54.2,1,1,0,0,0,-34.8,34.6);

	var maskedShapeInstanceList = [this.instance_59];

	for(var shapedInstanceItr = 0; shapedInstanceItr < maskedShapeInstanceList.length; shapedInstanceItr++) {
		maskedShapeInstanceList[shapedInstanceItr].mask = mask_1;
	}

	this.timeline.addTween(cjs.Tween.get(this.instance_59).to({y:249.8},9,cjs.Ease.get(1)).wait(491));

	// yellow floor
	this.shape = new cjs.Shape();
	this.shape.graphics.f("rgba(255,255,0,0.2)").s().p("EgkHgJ1MA2ugYMIRhAAMAAABEDg");
	this.shape.setTransform(385.5,196.4);

	this.timeline.addTween(cjs.Tween.get(this.shape).wait(500));

	// floor
	this.instance_60 = new lib.floor("synched",0);
	this.instance_60.parent = this;
	this.instance_60.setTransform(275,200);

	this.timeline.addTween(cjs.Tween.get(this.instance_60).wait(494).to({startPosition:0},0).wait(6));

}).prototype = p = new cjs.MovieClip();
p.nominalBounds = new cjs.Rectangle(299.9,81.4,616.8,638.5);
// library properties:
lib.properties = {
	width: 600,
	height: 480,
	fps: 30,
	color: "#CCD1DB",
	opacity: 1.00,
	manifest: [],
	preloads: []
};




})(lib = lib||{}, images = images||{}, createjs = createjs||{}, ss = ss||{}, AdobeAn = AdobeAn||{});
var lib, images, createjs, ss, AdobeAn;