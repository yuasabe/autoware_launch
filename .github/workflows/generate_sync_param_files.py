import glob
import yaml

def main():
    tier4_launch_path = "/home/minoda/git/autoware/src/universe/autoware.universe/launch/"
    files = glob.iglob(tier4_launch_path + '**/*.param.yaml', recursive=True)

    src2dst = []
    for src in files:
        dst_list = ['autoware_launch', 'config'] + src.split('/')[9:]
        dst = ''
        for el in dst_list:
            dst += el + '/'
        dst = dst[:-1]
        src2dst.append({
            "source": src,
            "dest": dst
        })
    
    sync_param_file = [{
        "repository": "autowarefoundation/autoware.universe",
        "files": src2dst
    }]

    with open("sync-param-files.yaml", "w") as f:
        yaml.dump(sync_param_file, f, sort_keys=False)

if __name__ == "__main__":
    main()
