import requests
import os
import sys
import time
import datetime

start = time.mktime(time.localtime())

t = datetime.datetime.now()
today = t.strftime('%m-%d-%Y')
vm_name = "Kali-%s" % today

url = 'https://images.offensive-security.com/\
virtual-images/kali-linux-2019.3-vbox-amd64.ova'

local_filename = url.split('/')[-1]


def download_file(url):
    if os.path.exists(local_filename):
        print('[*] Kali OVA Already Downloaded.')
    else:
        print('[*] Downloading Kali OVA...')
        with open(local_filename, 'wb') as f:
            response = requests.get(url, stream=True)
            total = response.headers.get('content-length')
            if total is None:
                f.write(response.content)
            else:
                downloaded = 0
                total = int(total)
                for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                    downloaded += len(data)
                    f.write(data)
                    done = int(50*downloaded/total)
                    sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50-done)))
                    sys.stdout.flush()
        sys.stdout.write('\n')
        return
        return local_filename
        print('[*] Done!')


def build_kali_vm():
    print('[*] Configuring Kali VM.')
    cmd = ("vboxmanage import %s --vsys 0 --vmname %s > /dev/null 2>&1" % (local_filename, vm_name))
    os.system(cmd)
    clipboardon = "vboxmanage modifyvm %s --clipboard bidirectional" % vm_name
    os.system(clipboardon)
    scalescreen = "VBoxManage setextradata %s GUI/ScaleFactor 2.5" % vm_name
    os.system(scalescreen)


def update_vm():
    print('[*] Starting Kali VM Headless.')
    startvmheadless = "VBoxManage startvm %s --type headless > /dev/null 2>&1 " % vm_name
    os.system(startvmheadless)
    time.sleep(45)
    print('[*] Updating Kali VM')
    cmd = 'VBoxManage guestcontrol %s run --quiet --verbose --exe "/bin/bash"\
    --username root --password toor --wait-stdout -- "/bin/bash" "-c"\
    "apt-mark hold virtualbox* > /dev/null 2>&1\
    && apt-get update > dev/null 2>&1\
    && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade > dev/null 2>&1\
    && apt-mark unhold virtualbox* > /dev/null 2>&1"' % vm_name
    os.system(cmd)
    print('[*] Rebooting Kali VM.')
    stopvm = 'VBoxManage controlvm %s poweroff > /dev/null 2>&1' % vm_name
    os.system(stopvm)
    time.sleep(30)
    print('[*] Rebooting Kali VM.')


def main():
    download_file(url)
    build_kali_vm()
    update_vm()
    stop = time.mktime(time.localtime())
    elapsed = datetime.timedelta(seconds=stop-start)
    print('[*] %s Took %s To Build.' % (vm_name, elapsed))
    startvm = "VBoxManage startvm %s> /dev/null 2>&1 " % vm_name
    os.system(startvm)


main()
