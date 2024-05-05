import resource

MB = 2**20

resource.setrlimit(resource.RLIMIT_AS, (20 * MB, 20 * MB))
resource.setrlimit(resource.RLIMIT_CPU, (300, 300))
