# a lot of these are probably not their true extension, but helps
# identify what type of file it is based on the file's header.
EXTENSIONS = {
    b"\x45\x56\x54\x58\x10\x00\x00": ".etp",  # dialog files
    b"\x53\x45\x44\x42\x6C\x79\x62": ".sedblyb",
    b"\x61\x73\x74\x62\x01\x00\x00": ".astb",
    b"\x61\x73\x74\x62\x02\x00\x00": ".astb",
    b"\x61\x73\x74\x62\x03\x00\x00": ".astb",
    b"\x61\x73\x74\x62\x04\x00\x00": ".astb",
    b"\x53\x45\x44\x42\x52\x45\x53": ".rps",  # SEDBRES
    b"\x89\x50\x4E\x47\x51\x01\x01": ".png_inval",  # real png, but they all appear to be encrypted
    b"\x6D\x64\x6C\x62\x01\x00\x00": ".mdlb",
    b"\x6D\x64\x6C\x62\x02\x00\x00": ".mdlb",
    b"\x64\x65\x66\x62\x03\x00\x00": ".defb",
    b"\x64\x65\x66\x62\x02\x00\x00": ".defb",
    b"\x44\x44\x53\x20\x7C\x00\x00": ".dds",
    b"\x3C\x3F\x78\x6D\x6C\x20\x76": ".xml",
    b"\xEF\xBB\xBF\x3C\x3F\x78\x6D": ".xml",
    b"\x45\x46\x58\x30\x30\x31\x31": ".efx",
    b"\x53\x45\x44\x42\x74\x78\x62": ".sedbtxb",
    b"\x63\x6C\x74\x00\x01\x00\x00": ".clt",
    b"\x23\x66\x69\x6C\x65\x53\x65": ".fileset",
    b"\x47\x72\x6F\x75\x70\x2C\x31": ".group",
    b"\x53\x45\x44\x42\x44\x53\x42": ".sedbdsb",
    b"\x53\x45\x44\x42\x53\x43\x42": ".sedbscb",
    b"\x53\x45\x44\x42\x53\x53\x43": ".scd",  # SEDBSSCF files, which are audio. can play them in vgmstream
    b"\x32\x30\x31\x30\x30\x31\x31": ".20100114",  # not sure what this is
    b"\x3C\x52\x70\x73\x50\x72\x6F": ".xml",  # this is an <RpsProject> file, but it's an xml
    b"\x43\x52\x59\x09":             ".cry",  # CRY file, which is encrypted.
    b"\x4D\x4C\x42\x44\x02\x00\x00": ".mlbd"
}
