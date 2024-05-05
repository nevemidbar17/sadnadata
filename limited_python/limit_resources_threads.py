import resource

MB = 2**20

resource.setrlimit(resource.RLIMIT_AS, (50 * MB, 50 * MB))
