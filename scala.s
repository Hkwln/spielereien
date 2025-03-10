        .section .data
message:
        .ascii "Hello, World!\n"
message_end:
        .set message_length, message_end - message

        .section .text
        .global _start

_start:
        # Write the message to stdout (file descriptor 1)
        mov $4, %eax                # System call number for sys_write
        mov $1, %ebx                # File descriptor 1 is stdout
        mov $message, %ecx          # Pointer to the message
        mov $message_length, %edx   # Length of the message
        int $0x80                   # Call kernel

        # Exit the program
        mov $1, %eax                # System call number for sys_exit
        mov $0, %ebx                # Return code 0 (success)
        int $0x80                   # Call kernel