# Cloudstack UI Cleaner

The container does background cleaning for data volumes and security groups which are broken after virtual machine object removal from the Cloudstack UI.

Known to work with:
 - Apache Cloudstack 4.9 with basic zone with security groups

Usage:

```
# docker pull bwsw/cloudstack-ui-cleaner
# docker run --restart=always -d --name cs-ui-cleaner \
             -e PAUSE=60 \
             -e CS_API_ENDPOINT=http://cshost/client/api \
             -e CS_API_KEY=key \
             -e CS_API_SECRET=secret \
             -e VOLUME_REMOVE_DELAY_MINUTES=2 \
             -e TAG_KEY=status \
             -e TAG_VALUE=removed \
             -e DEBUG=true \
             bwsw/cloudstack-ui-cleaner
```

## Container Parameters

Container supports next configuration parameters:

- PAUSE - interval between cleaning iterations
- CS_API_ENDPOINT - url of ACS API
- CS_API_KEY - key for ACS API
- CS_API_SECRET - secret for ACS API
- VOLUME_REMOVE_DELAY - which time must pass in minutes to remove the volume (must be greater than ACS expunge time)
- TAG_KEY - which tag to check in Volumes and SGs
- TAG_VALUE - which value must be set to purge
- DEBUG - print or avoid JSON dumps inside docker container (useful for troubleshooting in attached mode)
