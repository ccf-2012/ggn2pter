import os
import torclient
import constant
import argparse

TORRENT_DIR = constant.torrent_dir

parser = argparse.ArgumentParser(
    description='Search and add torrent to the qb client.')
parser.add_argument('-t', '--tor-name', required=False, help='torrent name ')    
ARGS = parser.parse_args()


def ensureDir(file_path):
    if os.path.isfile(file_path):
        file_path = os.path.dirname(file_path)
    if not os.path.exists(file_path):
        os.makedirs(file_path)


def add_torrent_to_qb(torrent_file):
    cs = torclient.ClientSetting()
    cs.load_from_config('config.ini')
    print('种子加入下载器...')
    dlclient = torclient.getDownloadClient(cs)
    st = None
    if dlclient:
        st = dlclient.addTorrentFile(torrent_file, '')
        if st:
            print('种子加入下载器成功: %s (%s) ' % (st.name, st.tracker))
    return st
 
def search_torrent(tor_path, tor_name):
    for fn in os.listdir(tor_path):
        if tor_name in fn:
            add_torrent_to_qb(os.join(tor_path, fn))
            return 

def add_torrents():
    ptertors = os.path.join(TORRENT_DIR, 'pter')
    backuptors = os.path.join(TORRENT_DIR, 'backup')
    ensureDir(backuptors)
    for fn in os.listdir(ptertors):
        add_torrent_to_qb(os.path.join(ptertors, fn))
        os.rename(os.path.join(ptertors, fn), os.path.join(backuptors, fn))


def main():
    # search_torrent(os.path.join(TORRENT_DIR, 'pter'), ARGS.tor_name)
    add_torrents()


if __name__ == '__main__':
    main()