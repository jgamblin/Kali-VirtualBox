# Kali VirtualBox

A simple python script to automatically download, provision and update a [Kali Linux](https://www.kali.org/) VM in [Virtualbox](https://www.virtualbox.org/).

## Usage
`./python3 KaliVM.py`

## Sample Output
![](https://jerrygamblin.com/wp-content/uploads/2019/07/Screen-Shot-2019-07-08-at-9.13.40-AM.png)
_I couldn't get guestcontrol to be quite so the output is a little off._

## Requirements
*   Requires [Oracle VM VirtualBox](https://www.virtualbox.org/)
*   Requires [Oracle VM VirtualBox Extension Pack](https://www.virtualbox.org/wiki/Downloads)
*   Requires Python `requests`.
    -   Install Via `pip install -r requirements.txt`

## Notes
*   Creates A VM named `Kali-Day-Month-Year`
*   Can Use Over 4GB of Data (Watch On Metered Connections).
*   Takes 30+ Minutes To Build Depending On Connection Speed.,
