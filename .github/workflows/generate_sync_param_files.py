import glob
import yaml
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=str)
    args = parser.parse_args()

    tier4_launch_path = "/tmp/autoware.universe/launch/"
    files = glob.iglob(tier4_launch_path + '**/*.param.yaml', recursive=True)

    src2dst = []
    for file in files:
        src_list = file.split('/')[3:]
        dst_list = ['autoware_launch', 'config'] + file.split('/')[4:5] + file.split('/')[6:]
        src = ''
        for el in src_list:
            src += el + '/'
        src = src[:-1]
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

    with open(args.output, "w") as f:
        yaml.dump(sync_param_file, f, sort_keys=False)

if __name__ == "__main__":
    main()
