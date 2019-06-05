# ES6基本语法

## 环境搭建
**node.js不直接支持es6语法，需要前期一些准备**
### 必备包安装
```
1. 全局安装es-checker
	npm install -g es-checker
	查看Node.js对ES6的支持情况
	es-checker 
2. 安装babel-core
	npm install babel-core --save
3. 安装babel-preset-es2015
	npm install babel-preset-es2015
```
### 项目搭建
```
1. 进入指定目录
2. npm init初始化工作目录
	npm init -y
3. 本地安装Babel-cli(也可以选择全局安装)
	// 本地安装
	npm install babel-cli -g
	// 本地安装
	npm install babel-cli --save
4. 安装babel-preset-es2015来支持ES6的语法
	npm install babel-preset-es2015 --save
5. 创建一个名为.babelrc的配置文件，方便babel-cli使用babel-preset-es2015
	文件创建注意事项，windows不支持".babelrc"直接命名方式，需要采用".babelrc."
	文件内容
	{
		"presets": [
			"es2015"
		],
		"plugins": []
	}
```
### 测试项目
```
1. 创建测试文件一(app.js)
	export var m = 10
2. 创建测试文件二(test.js)
	import {m} from './app'
	console.log(m)
3. 运行测试
	不能执行运行"node test.js"，否则会报错
	3.1. 当"babel-cli"全局安装，可以直接运行
		babel-node test.js
	3.2. 当"babel-cli"本地安装时
		1) 在package.json文件的scripts添加命令"babel": "babel-node test.js"
		2) 执行"npm run babel"
```

## let与const

### let
let 声明的变量只在 let 命令所在的代码块内有效。

#### 代码块内有效
```javascript
{
  let a = 0;
  var b = 1;
}
a  // ReferenceError: a is not defined
b  // 1
```

#### 不能重复声明
let 只能声明一次 var 可以声明多次
```javascript
let a = 1;
let a = 2;
var b = 3;
var b = 4;
a  // Identifier 'a' has already been declared
b  // 4
```

#### 不存在变量提升
```javascript
console.log(a);  //ReferenceError: a is not defined
let a = "apple";
 
console.log(b);  //undefined
var b = "banana";
```

### const
const 声明一个只读变量，声明之后不允许改变。意味着，一旦声明必须初始化，否则会报错。

#### 不存在变量提升
代码块内如果存在 let 或者 const，代码块会对这些命令声明的变量从块的开始就形成一个封闭作用域。代码块内，在声明变量 PI 之前使用它会报错。
```javascript
var PI = "a";
if(true){
  console.log(PI);  // ReferenceError: PI is not defined
  const PI = "3.1415926";
}
```

#### 注意要点
javascript的const类似于C、c++中的指针常量(int * const p //指针常量),指向的地址不能改，地址中的数据可以改
const 如何做到变量在声明初始化之后不允许改变的？其实 const 其实保证的不是变量的值不变，而是保证变量指向的内存地址所保存的数据不允许改动。此时，你可能已经想到，简单类型和复合类型保存值的方式是不同的。是的，对于简单类型（数值 number、字符串 string 、布尔值 boolean）,值就保存在变量指向的那个内存地址，因此 const 声明的简单类型变量等同于常量。而复杂类型（对象 object，数组 array，函数 function），变量指向的内存地址其实是保存了一个指向实际数据的指针，所以 const 只能保证指针是固定的，至于指针指向的数据结构变不变就无法控制了，所以使用 const 声明复杂类型对象时要慎重。

## export

### export default详解

#### 基本用法
**使用import命令的时候，用户需要知道所要加载的变量名或函数名，否则无法加载。**但是，用户肯定希望快速上手，未必愿意阅读文档，去了解模块有哪些属性和方法。**为了给用户提供方便，让他们不用阅读文档就能加载模块，就要用到export default命令，为模块指定默认输出。**
```javascript
//1. port-default.js
//export-default.js 这是一个模块文件export-default.js，它的默认输出是一个函数
export default function () {
  console.log('foo');
}

//2. import-default.js
import customName from './export-default';
customName();  //'foo'
//这是的import命令，可以用任意名称指向export-default.js输出的方法，这时就不需要知道原模块输出的函数名。
//需要注意的是，这时import命令后面，不使用大括号。
```

#### 用在非匿名函数前
```javascript
//1. export-default.js
export default function foo() {
  console.log('foo');
} 
// 或者写成 
function foo() {
  console.log('foo');
} 
export default foo;
//上面代码中，foo函数的函数名foo，在模块外部是无效的。加载的时候，视同匿名函数加载。
```

#### 与export的区别
第一组是使用export default时，对应的import语句不需要使用大括号； 
第二组是不使用export default时，对应的import语句需要使用大括号。 
export default命令用于指定模块的默认输出。显然，一个模块只能有一个默认输出，因此export default命令只能使用一次。所以，import命令后面才不用加大括号，因为只可能唯一对应export default命令。
```javascript
// 第一组
export default function crc32() { // 输出
  // ...
}
import crc32 from 'crc32'; // 输入 
// 第二组
export function crc32() { // 输出
  // ...
};
import {crc32} from 'crc32'; // 输入
```

#### 用在变量前
export default就是输出一个叫做default的变量或方法，然后系统允许你为它取任意名字
```javascript
// 正确
export var a = 1; 
// 正确
var a = 1;
export default a; 
// 错误
// 代码中，export default a的含义是将变量a的值赋给变量default。所以，最后一种写法会报错。
export default var a = 1;
// 错误
var a = 1;
export a;
// 正确
var a = 1;
export {a}
```

#### 用在值前
因为export default 命令的本质是将后面的值，赋给default变量，所以可以直接将一个值写在export default之后
```javascript
// 正确
export default 42; 
// 报错 原因这一句报错是因为没有指定对外的接口，而前一句指定外对接口为default。
export 42;
```

#### 调用模块(import)
```javascript
//1. export default命令，输入模块时就非常直观了，以输入 lodash 模块为例
import _ from 'lodash';
//2. 如果想在一条import语句中，同时输入默认方法和其他接口，可以写成下面这样
import _, { each, each as forEach } from 'lodash';
//3. lodash.js文件内容
export default function (obj) {
  // ···
} 
export function each(obj, iterator, context) {
  // ···
}
export { each as forEach };//暴露出forEach接口，默认指向each接口，即forEach和each指向同一个方法。
```

#### 用在类前
```javascript
// MyClass.js
export default class { ... }
 
// main.js
import MyClass from 'MyClass';
let o = new MyClass();
```



