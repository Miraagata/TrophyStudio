#pragma once
#include <psp2kern/types.h>
#include "vcng_kernel_io_wire.h"
int vcngKernelMemcpyForce(void *dst, const void *src, int size, int flush);
int vcngKernelMemcpySafe(void *dst, const void *src, int size);
int vcngKernelPeekButtons(void);
int vcngKernelIoMkdir(const char *path, int mode);
SceUID vcngKernelIoOpen(const char *path, int flags, int mode);
int vcngKernelIoClose(SceUID fd);
int vcngKernelIoRead(SceUID fd, void *dst, int len);
int vcngKernelIoWrite(SceUID fd, const void *src, int len);
int vcngKernelIoPread(SceUID fd, void *dst, int len, SceOff offset);
int vcngKernelIoPwrite(SceUID fd, const void *src, int len, SceOff offset);
SceOff vcngKernelIoLseek(SceUID fd, SceOff offset, int whence);
int vcngKernelIoSyncByFd(SceUID fd);
int vcngKernelIoRemove(const char *path);
int vcngKernelIoRename(const char *old_path, const char *new_path);
int vcngKernelIoGetstat(const char *path, vcng_stat_wire *user_stat);
SceUID vcngKernelIoDopen(const char *path);
int vcngKernelIoDread(SceUID fd, vcng_dirent_wire *user_dirent);
int vcngKernelIoDclose(SceUID fd);
void vcng_kernel_api_init(void);

void vcng_kernel_set_allowed_pid(SceUID pid);
