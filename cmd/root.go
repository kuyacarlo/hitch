package cmd

import (
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
	Use:   "hitch",
	Short: "Convert compose files to Podman quadlet units",
	Long:  "hitch converts Docker Compose files into systemd units managed by Podman, handling install, enable, disable, and lifecycle operations.",
}

func init() {
	rootCmd.PersistentFlags().Bool("user", true, "operate in user mode (systemctl --user)")
	rootCmd.PersistentFlags().Bool("system", false, "operate in system mode")
}

// SetVersion sets the version string displayed by --version.
func SetVersion(v string) {
	rootCmd.Version = v
}

// Execute runs the root command. Called from main.go.
func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}

// getSystem returns whether system mode is active.
// --system=true takes precedence; otherwise it's the inverse of --user.
func getSystem(cmd *cobra.Command) bool {
	systemFlag, _ := cmd.Flags().GetBool("system")
	if systemFlag {
		return true
	}
	userFlag, _ := cmd.Flags().GetBool("user")
	return !userFlag
}
