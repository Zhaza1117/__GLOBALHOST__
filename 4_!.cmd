AL_FIN(__GLOBALHOST__::@(WUNDOW)){
	__AI__::__DATAMINER__:@(__LOCALIZEDHOST__)+=[%HOST%]
	__AI__::__COUNTERMEASURE__:@(__ACTION__){
		SCRAMBLE:@(0101 1100 1010 1011 1110 0010 0101 0010 1010 1011 1101 0100 1010 0001 0000 1111)+=[%HOST%]
		__MODEMSYSTEM__::__MODULATION__:_#[5002.01112 kps]-^//tty://echo@01011100/backbone/c1/0001/0000/0011/0000
		__SYSTEMCHECK__:@(__ERRORLEVEL__)+=__CONNECTION__:#_:[__IPADDRESS__:_$[0.0.0.0]]
		__COMMANDLINE__::_#[assoc *USR prompt *DOMAIN -ns -v 0.0.0.0]
	}
	
	__CONNECTION__::__ACTION__:?_:@(__GLOBALHOST__) != errorlevel
	__DATASTREAM__::__FINDSYSTEM__:?_#[GOVNA-2201]+=[%HOST%]
	__DATASTREAM__::__FINDSYSTEM__:?_#[DENVOR-2013]+=[%HOST%]
	__DATAMINER__+=[CENTRA.IRGO.AEGI]
	
	
	__ACTION__:@(__COUNTERMEASURE__){
		SCRAMBLE:@(HECTOR ALPHA BRAVO DELTA MINOR HOTEL BRAVO ECHO DELTA NINE FIVE ZERO DELTA HOTEL OMEGA)
		FOR X%% verify : assoc *USR netsh *DOMAIN -xcopy [%HOST%] X++
		__AI__::__NETOWRBIND__:@(__ACTION__)
		__MODEMSYSTEM__:@(URL:/KPDB.SS2)
		_$://HOTKEY!@DENVOR-2013
		
	}
}