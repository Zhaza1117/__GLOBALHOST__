//
// wpad.dat script FOR SYRACUSE - Proxy IP: 75.104.128.60
//

var firstrun;                       // Flag to indicate if the browser was just launched
var unprovisioned = false           // Unprovisioned account flag
var proxyhost = "75.104.128.60:80"; // Proxy host
var myip = "";

function FindProxyForURL(url,host) {
        if (myip != myIpAddress()) {
                firstrun = true;
        }
        myip = myIpAddress();

        // If CPE has a private IP, verify if we are unprovisioned
        if (firstrun && isPrivateIp(myip)) {
                var ip = dnsResolve("www.wildblue.net");
                if (ip == "10.255.10.40") {
                        // unprovisioned account
                        unprovisioned = true;
                }
        }

        // If the CPE has a routable IP, the account is in provisioned state
        if (!isPrivateIp(myip)) unprovisioned = false;
        firstrun = false;

        // determine if the proxy should be used
        if (dnsDomainIs(host, "backoffice.wildblue.net") || // destination is WildBlue backoffice
            isPrivateIp(host) ||                            // destination is in the private IP domain
            isPlainHostName(host) ||                        // destination is in the local network
            unprovisioned         ||                        // unprovisioned account
            myip == "127.0.0.1"   ||                        // no CPE IP, disable proxy
            url.substring(0, 6) == "https:"                 // destination is an SSL site
        ) {
                return "DIRECT";
        } else {
                return "PROXY " + proxyhost;
        }
}

function isPrivateIp(ip) {
        if (!ip.match(/^\d+\.\d+\.\d+\.\d+$/)) return false;

        if (isInNet(ip, "192.168.0.0", "255.255.0.0") ||
            isInNet(ip, "172.16.0.0", "255.255.0.0") ||
            isInNet(ip, "172.17.0.0", "255.255.0.0") ||
            isInNet(ip, "10.0.0.0", "255.0.0.0"))
        return true;

        return false;
}

